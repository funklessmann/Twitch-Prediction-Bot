import time, sys
from csv import DictReader

"""
    # forked from: https://github.com/jeff502/Twitch-Prediction-Bot
    # loaded into VSCode with python 3.11.1
    # created a 
    
py -m venv .venv

    # and then ran the below libraries
    # ensure that you run 
    
python.exe -m pip install --upgrade pip
pip install selenium  
pip install webdriver_manager 

    # before execution, add the cookies to twitch_cookies.csv (retain first line for header)
    # I installed https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid
    # to get the cookies, exported to TXT and then rearranged the columns in excel to get the 
    
name,value,domain

    # in the right order
"""

from selenium import webdriver
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        NoSuchElementException,
                                        StaleElementReferenceException)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from point_logic import get_points, how_much_to_bet, time_set
from prediction_logic import check_prediction_history, prediction_history
from xpath_and_css_selectors import *

CHANNEL_NAME = "leopard"
STREAMER = f"https://www.twitch.tv/popout/{CHANNEL_NAME}/chat"

# percent_amount = 0.0625 - six percent
percent_amount = 0.055 # five percent

ser = Service("C:\Program Files (x86)\webdriver\chromedriver.exe")
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


def get_cookie_values(file):
    """
    Takes all the cookies from our csv file.
    Turns them into a list of dicts
    :param file: csv file
    :return: a list of dicts
    """
    with open(file, encoding="utf-8-sig") as f:
        dict_reader = DictReader(f)
        list_of_dicts = list(dict_reader)
    return list_of_dicts


def upload_cookies():
    """
    Reads and adds cookies to our browser. Refreshes the page when it's done.
    """
    cookies = get_cookie_values("twitch_cookies.csv")
    for i in cookies:
        driver.add_cookie(i)

    driver.refresh()


if __name__ == "__main__":
    driver.get(STREAMER)
    upload_cookies()
    if check_prediction_history(CHANNEL_NAME):
        total_before_bets, current_loop_count, the_percent = check_prediction_history(
            CHANNEL_NAME)
    else:
        the_percent = 1
        current_loop_count = 1
        total_before_bets = 0

    high_score = 0
    while True:
        try:
            time.sleep(2)
            channel_points = driver.find_element(
                By.CSS_SELECTOR, my_channel_points)
            channel_points.click()
            time.sleep(2)

            try:
                driver.find_element(By.XPATH, getting_started_prompt).click()
            except NoSuchElementException as e:
                pass

            time.sleep(2)
            driver.find_element(By.XPATH, channel_prediction_prompt).click()

            is_submission_closed = driver.find_element(
                By.CSS_SELECTOR, submission_text
            ).text.lower()

            if "closed" in is_submission_closed:
                try:
                    driver.find_element(By.XPATH, x_button).click()
                except NoSuchElementException as e:
                    pass
                time.sleep(30)
                continue
            elif "ended" in is_submission_closed:
                try:
                    driver.find_element(By.XPATH, x_button).click()
                except NoSuchElementException as e:
                    pass
                time.sleep(30)
                continue
            else:
                pass

            try:
                my_points = driver.find_element(By.XPATH, points_xpath).text
                total_points = get_points(my_points)

                if total_points >= 250000:
                    points = 250000
                else:
                    points = total_points

                if total_points > high_score:
                    high_score = total_points

                if total_before_bets == 0:
                    total_before_bets = total_points

                if total_before_bets < total_points:
                    current_loop_count = 1
                    total_before_bets = total_points

                if current_loop_count > 4:
                    current_loop_count = 1
                    the_percent = (round(points * percent_amount))
                    total_before_bets = total_points

                elif current_loop_count == 1:
                    the_percent = (round(points * percent_amount))

                points_to_bet = how_much_to_bet(
                    the_p=the_percent, current_loop=current_loop_count)

            except NoSuchElementException as e:
                try:
                    driver.find_element(By.XPATH, x_button).click()
                except NoSuchElementException as e:
                    continue
                continue

            total_time_remaining = driver.find_element(By.XPATH, timer).text
            total_time_for_func = total_time_remaining.split()[0]
            time_set(total_time_for_func)
            time.sleep(2)

            tbv = driver.find_element(By.XPATH, blue_votes).text
            trv = driver.find_element(By.XPATH, red_votes).text

            if tbv == "":
                total_blue_votes = 0
            else:
                total_blue_votes = get_points(tbv)

            if trv == "":
                total_red_votes = 0
            else:
                total_red_votes = get_points(trv)

            driver.find_element(By.XPATH, channel_points_reward_body).click()
            if total_blue_votes > total_red_votes:
                red = driver.find_element(By.XPATH, red_field)
                red.click()
                red.send_keys(points_to_bet)
                time.sleep(2)
                red_vote_button = driver.find_element(By.XPATH, red_button)
                red_vote_button.click()
                time.sleep(2)
                prediction_history(CHANNEL_NAME, points_to_bet, "Red",
                                   current_loop_count, total_before_bets, the_percent)

                current_loop_count += 1
                driver.find_element(By.XPATH, red_end).click()
            else:
                blue = driver.find_element(By.XPATH, blue_field)
                blue.click()
                blue.send_keys(points_to_bet)
                time.sleep(2)
                blue_vote_button = driver.find_element(By.XPATH, blue_button)
                blue_vote_button.click()
                time.sleep(2)
                prediction_history(CHANNEL_NAME, points_to_bet, "Blue",
                                   current_loop_count, total_before_bets, the_percent)

                current_loop_count += 1
                driver.find_element(By.XPATH, blue_end).click()
        except (NoSuchElementException, ElementClickInterceptedException) as e:
            pass
        except StaleElementReferenceException:
            driver.refresh()

        time.sleep(30)
