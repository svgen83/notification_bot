# Notification_bot
This is a program of timely student review information ["Devman"](https://dvmn.org/) from course instructors. 

### How to setup

Python3 must already be installed.
Then use `pip` (or` pip3` if there is a conflict with Python2) to install the dependencies:
```
pip install -r requirements.txt
```
#### Program settings

In order for the program to work correctly, in the program folder, create an .env file containing the site token ["Devman"] (https://dvmn.org/).
You can get it in the [section with API documentation] (https://dvmn.org/api/docs/).

Write it like this:

```
DEVMAN_TOKEN="Devman token"
```
Also, in the .env file, you must register the telegram bot token and your own chat-id:
```
TG_TOKEN="Telegram bot token"
TG_CHAT_ID="own chat-id"
```

You will receive a token when registering a bot. It says here [how to register a telegram bot](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram/).
You can get information about your own chat-id using telegram bots created for this purpose. For example, Get My ID.


#### How to run

The program runs from the command line. To run the program using the cd command, you first need to go to the folder with the program.
To run the program on the command line, write:
```
python bot.py
```
When the result of the verification of the work appears, a message about this will come to your telegram.

To run the program from the server, you must first acquire a server. The following is an example of running on a Heroku virtual server. The first step is to register on the [Heroku website](https://heroku.com) and create an app. You can submit the code from GitHub. After linking your GitHub account to Heroku, you should find the repository with the code and connect it to Heroku. The token and chat-id should be specified in the Config Vars section in the Settings tab. Click the "Deploy Branch" button.

### Project goal

The code is written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/).
