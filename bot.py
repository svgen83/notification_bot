import os

import requests

import telegram

import time

from dotenv import load_dotenv

from textwrap import dedent


def create_messages(reply):
    new_attempts = reply['new_attempts']
    messages = []
    for new_attempt in new_attempts:
        for subject, description in new_attempt.items():
            lesson_title = new_attempt['lesson_title']
            lesson_url = new_attempt['lesson_url']
            negative = new_attempt['is_negative']
            if negative:
              message = dedent(f'''
                    У вас проверили работу
                    {lesson_title}
                    К сожалению, в работе нашлись ошибки
                    {lesson_url}
                    ''')
            else:
              message = dedent(f'''
                     У вас проверили работу
                     {lesson_title}
                     Преподавателю всё понравилось, 
                     можно приступать к следующему уроку
                     {lesson_url}
                     ''')
            messages.append(message)
    return messages


def get_timestamp(reply):
    if reply['status'] == 'found':
        timestamp = reply['last_attempt_timestamp']
    elif reply['status'] == 'timeout':
        timestamp = reply['timestamp_to_request']
    return timestamp


if __name__ == '__main__':

    load_dotenv()

    TG_TOKEN = os.getenv('TG_TOKEN')
    TG_CHAT_ID = os.getenv('TG_CHAT_ID')
    DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')

    lp_url = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': DEVMAN_TOKEN}
    timeout = 90
    timer = 30
    timestamp = 0
    params = {}
    bot = telegram.Bot(token=TG_TOKEN)

    while True:
        try:
            response = requests.get(lp_url,
                                    timeout=timeout,
                                    params=params,
                                    headers=headers)
            response.raise_for_status()
            reply = response.json()
            timestamp = get_timestamp(reply)
            params.update({"timestamp": timestamp})
            if reply['status'] == 'found':
              messages = create_messages(reply)
              for message in messages:
                  bot.send_message(chat_id=TG_CHAT_ID, text=message)
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            print("Отсутствует интернет-подключение")
            time.sleep(timer)
