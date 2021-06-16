This is a custom telegram bot made with python library telegram-python-bot.

It's written with the following dependencies:
python-telegram-bot==13.3

There are two ways to install and run this bot.

Option 1 - Clean Python interpreter (Linux):

Installation:
1. $sudo apt-get install python3 python3-pip git-all
2. Pull git repo into any directory, - $git clone https://github.com/gregsavvy/Python_telegramBot.git
3. From main directory, - $pip3 install --no-cache-dir -r requirements.txt

Run:
1. From main directory, - $python3 main.py
2. Now you can find the bot in telegram, - @movie_ref_bot

Option 2 - Docker (Linux):

Installation:
1. Install Docker, - $sudo apt-get install docker-ce docker-ce-cli containerd.io
2. Install Git, - $sudo apt-get install git-all
3. Pull git repo into any directory, - $git clone https://github.com/gregsavvy/Python_telegramBot.git
4. From main directory, - $sudo docker build -t telegrambotpy .

Run:
1. $sudo docker run telegrambotpy
