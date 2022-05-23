import requests
from flask import current_app
from flasksite.views.bot.controllers.bot_utilities import createKeyboardMarkup


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


def sendMessageWithKeyboard(chat_id, text, buttons):
    return requestToTelegram("sendMessage", {"chat_id": chat_id, "text": text, "reply_markup": createKeyboardMarkup(buttons)})


def sendDocument(chat_id, document):
    return requestToTelegram("sendDocument", {"chat_id": chat_id, "document": document})


def deleteMessage(chat_id, message_id):
    return requestToTelegram("deleteMessage", {"chat_id": chat_id, "message_id": message_id})