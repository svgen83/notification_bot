import os

import requests

import telegram

from dotenv import load_dotenv


def choose_message(reply):
    lesson_title = '"' + reply['new_attempts'][0]["lesson_title"] + '"'
    lesson_url = reply['new_attempts'][0]['lesson_url']
    positive_msg_template = f'''У вас проверили работу 
    {lesson_title}
    Преподавателю всё понравилось, можно приступать к следующему уроку
    {lesson_url}'''
    negative_msg_template = f'''У вас проверили работу
    {lesson_title}
    К сожалению, в работе нашлись ошибки
    {lesson_url}'''
    if reply['new_attempts'][0]['is_negative']:
        message = negative_msg_template
    else:
        message = positive_msg_template
    return message


if __name__ == '__main__':

    load_dotenv()

    TG_TOKEN = os.getenv('TG_TOKEN')
    TG_CHAT_ID = os.getenv('TG_CHAT_ID')
    DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')

    lp_url = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': DEVMAN_TOKEN}
    timer = 90
    timestamp = 0
    params = {}
    bot = telegram.Bot(token=TG_TOKEN)

    while True:
        try:
            response = requests.get(lp_url,
                                    timeout=timer,
                                    params=params,
                                    headers=headers)
            response.raise_for_status()
            reply = response.json()
            timestamp = reply['last_attempt_timestamp']
            params.update({"timestamp": timestamp})
            message = choose_message(reply)
            bot.send_message(chat_id=TG_CHAT_ID, text=message)
        except requests.exceptions.ReadTimeout:
            print("новых работ нет")
        except requests.exceptions.ConnectionError:
            print("Отсутствует интернет-подключение")
