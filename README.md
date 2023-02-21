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
================
Cleaned up and refactored the code. \
Added a feature to continute your betting streak between streams. \

Update 2/21/2023 by funkless
============================

* forked from: https://github.com/jeff502/Twitch-Prediction-Bot \
* loaded into VSCode with python 3.11.1 \
* prepped to target twitch.tv/leopard (you can change this to a different streamer if you like, hemhem datto hemhem) \
* created a virtual environment with:
    
`     py -m venv .venv `

* ensure that you run
`    
     python.exe -m pip install --upgrade pip

     pip install selenium  

     pip install webdriver_manager 
`

...before execution, add the cookies to twitch_cookies.csv (see instructions above, retain first line for header). I installed https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid
to get the cookies, exported to TXT and then rearranged the columns in excel to get the 
    
`     name,value,domain `

...in the right order. Also a thing to watch out for is that you can ONLY use twitch.tv cookies, so things like gql.twitch.tv or passport.twitch.tv need to be taken out. Also, if your domain is showing at ".twitch.tv" ensure to change it to "twitch.tv" (no prepended period). \

* removed mentions from the code of defaulting to 6% of channel points \
* set the % you want to spend to the top of main.py \
* I also added a bunch more libraries at the top of the code to ensure the drivers are installed on execute, and switched it from a Chrome/Chromium build to a firefox build. I haven't tested what happens if you don't have Chrome and Firefox installed on your machine, so if you're having trouble start there, or if you hate firefox for some reason, go back to the original fork above. \

TO USE THIS CODE
================

You'll need to set up VSCode with python3 or a similar python interpreter, use the pip commands above to install the libraries, and then run it. Remember to install the libraries to your venv (virtual environment) before running, and ensure you're running main.py inside the venv as well. \

run with this command from the venv terminal, and in the directory: \
`
py main.py
`

Untested, so I don't know if it'll work, I'll update if it doesn't and I get it working. If you wanted to run this automatically you could probably create a chronjob or scheduled task in windows at 6:30am Eastern #neverlate #alwaysontime \
