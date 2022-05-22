from urllib.parse import urlparse
from flask import current_app
from flasksite.views.bot.controllers.telegram_api_functions import setupWebhook
from flasksite.views.bot.controllers.bot_commands import start
from flasksite.views.bot.controllers.bot_utilities import Message


def home_logic(request):
    if request.method == 'POST':
        print(request.json['message'])

        message = Message(request.json)

        if message.text == '/start':
            start(message.chat_id, message.username)
            
    return "OK"


def set_webhook_logic(request):
    parseResult = urlparse(request.base_url)
    url = "https://" + parseResult.hostname + "/" + current_app.config['TELEGRAM_TOKEN']
    return setupWebhook(url)