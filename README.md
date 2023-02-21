# Twitch-Prediction-Bot
A Selenium based webdriver used to automatically bet on Twitch Predictions.\
You'll need a Selenium webdriver inorder to run this program. `https://pypi.org/project/selenium/`\
Under `drivers` download the driver for your browser.\
This bot uses Google Chrome and Selenium's Chrome driver by default. Feel free to change this as you see fit.

This bot works by taking 6.25% of your current channel points and bets it on the option with the least votes at one minute remaining.\
Each time the bot fails to win, it'll double the current bet up to four total bets.\
Bets are recorded into a log file named `Twitch Prediction History.txt`.

The code is highly editable to fit your betting habits.
Change the `points_to_bet` variable to whatever you desire. \
Changing the default to either `blue` or `red` for always believing or doubting.


Change the `channel_name` to the streamer you want to use the bot on.\
Currently, this bot works on the pop out chat window. You can change this if desired.

You'll need to either upload your own cookies into the webdriver (recommended), or log in manually when the bot starts.

For uploading your own cookies, watch this Youtube video: https://youtu.be/vhjKJ7huN-w \
Put your cookies into the file named `twitch_cookies.csv`.

For logging in manually, set the intial sleep to two minutes and comment out lines `75` and uncomment  line `76`.\
`ctrl+/` to comment or uncomment. \


Update May-6 \
Cleaned up and refactored the code. \
Added a feature to continute your betting streak between streams. \

Update 2/21/2023

forked from: https://github.com/jeff502/Twitch-Prediction-Bot
loaded into VSCode with python 3.11.1
prepped to target twitch.tv/leopard
created a 
    
py -m venv .venv

and then ran the below libraries
ensure that you run 
    
python.exe -m pip install --upgrade pip

pip install selenium  

pip install webdriver_manager 

before execution, add the cookies to twitch_cookies.csv (retain first line for header)
I installed https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid
to get the cookies, exported to TXT and then rearranged the columns in excel to get the 
    
name,value,domain

in the right order
