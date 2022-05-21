from urllib.parse import urlparse
from flask import current_app
from flasksite.views.bot.controllers.telegram_api_functions import setupWebhook
from flasksite.views.bot.controllers.bot_commands import start


def home_logic(request):
    if request.method == 'POST':
        print(request.json['message'])
        try:
            message = request.json['message']
            try:
                chat_id = message['chat']['id']
                username = message['chat']['username']
                text = message['text']

                if text == '/start':
                    start(chat_id, username)
            except:
                chat_id = message['chat']['id']
                username = None
                text = message['text']

                if text == '/start':
                    start(chat_id, username)
        except Exception as e:
            print(e)
            pass
        return 'ok'
    return "OK"


def set_webhook_logic(request):
    parseResult = urlparse(request.base_url)
    url = "https://" + parseResult.hostname + "/" + current_app.config['TELEGRAM_TOKEN']
    return setupWebhook(url)