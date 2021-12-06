# Notification_bot
Эта программа предназначена для получения своевременной информации о проверке работ студентами ["Devman"](https://dvmn.org/) от преподавателей курса. 

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
#### Настройки программы

Для того, чтобы программа корректно работала, в папке с программой создайте файл .env, содержащий токен сайта ["Devman"](https://dvmn.org/). 
Получить его можно в [разделе с документацией по API](https://dvmn.org/api/docs/).

Пропишите его следующим образом:
```
DEVMAN_TOKEN="Токен Девмана"

```
Также в файле .env необходимо прописать токен телеграмм-бота и собственный chat-id:
```
TG_TOKEN="Токен телеграмм-бота"

TG_CHAT_ID="собственный chat-id"

```

Токен Вы получите при регистрации бота. Здесь написано [как зарегистрирвать телеграмм-бот](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram/).
Получить информацию о собственном chat-id можно с помощью телеграмм-ботов, созданных для этой цели. Например, Get My ID.


#### Как запустить

Программа запускается из командной строки. Для запуска программы с помощью команды cd сначала нужно перейти в папку с программой. 
Для запуска программы в командной строке пишем:
```
python bot.py
```
При появлении результата о проверке работ,  сообщение об этом придет на Ваш телеграмм.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).