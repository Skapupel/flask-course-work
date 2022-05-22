from urllib.parse import urlparse
from flask import current_app
from flasksite.views.bot.controllers.telegram_api_functions import setupWebhook
from flasksite.views.bot.controllers.bot_commands import start, username, after_username
from flasksite.views.bot.controllers.bot_utilities import Message
from flasksite.views.bot.controllers.telegram_api_functions import sendMessage
from flasksite.models import Users


def home_logic(request):
    if request.method == 'POST':
        print(request.json['message'])

        message = Message(request.json)
        user = Users.query.filter_by(chat_id=message.chat_id).first()

        if message.text == '/start':
            start(message.chat_id, message.username)
        else:
            if user:
                if message.text == '/username':
                    username(message.chat_id)


                elif user.menu == 'username':
                    after_username(user, message)
            else:
                sendMessage(message.chat_id, 'Ви не зареєстровані. Використовуйте команду /start')

    return "OK"


def set_webhook_logic(request):
    parseResult = urlparse(request.base_url)
    url = "https://" + parseResult.hostname + "/" + current_app.config['TELEGRAM_TOKEN']
    return setupWebhook(url)