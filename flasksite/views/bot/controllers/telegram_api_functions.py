import requests
from flask import current_app


def requestToTelegram(method, params=None):
    url = "https://api.telegram.org/bot" + current_app.config['TELEGRAM_TOKEN'] + "/" + method
    if params:
        response = requests.post(url, json=params)
    else:
        response = requests.get(url)
    return response.json()


def setupWebhook(url):
    return requestToTelegram("setWebhook", {"url": url})


def sendMessage(chat_id, text):
    return requestToTelegram("sendMessage", {"chat_id": chat_id, "text": text})