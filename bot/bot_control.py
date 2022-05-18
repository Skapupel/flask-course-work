import requests
from flasksite import app


def requestToTelegram(method, params=None):
    url = "https://api.telegram.org/bot" + app.config['TELEGRAM_TOKEN'] + "/" + method
    if params:
        r = requests.post(url, json=params)
    else:
        r = requests.get(url)
    return r.json()


def setupWebhook(url):
    return requestToTelegram("setWebhook", {"url": url})


def sendMessage(chat_id, text):
    return requestToTelegram("sendMessage", {"chat_id": chat_id, "text": text})