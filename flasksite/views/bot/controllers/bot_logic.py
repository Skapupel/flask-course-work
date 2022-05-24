from urllib.parse import urlparse
from flask import current_app
from flasksite.views.bot.controllers.telegram_api_functions import deleteMessage, setupWebhook
from flasksite.views.bot.controllers.bot_commands import start, username, after_username, password, after_password, bot_help
from flasksite.views.bot.controllers.bot_utilities import Message
from flasksite.views.bot.controllers.telegram_api_functions import sendMessage
from flasksite.models import Users


def home_logic(request):
    if request.method == 'POST':

        message = Message(request.json)

        user = Users.query.filter_by(chat_id=message.chat_id).first()

        if message.text == '/start' or message.data == 'start':
            start(user, message)
        else:
            if user:
                if message.text == '/username':
                    username(message.chat_id, user)
                elif message.text == '/password':
                    password(message.chat_id, user)
                elif message.text == '/help':
                    parseResult = urlparse(request.base_url)
                    url = "https://" + parseResult.hostname
                    bot_help(message.chat_id, user, url)


                elif user.menu == 'username':
                    after_username(user, message)
                elif user.menu == 'password':
                    after_password(user, message)
                

                else:
                    deleteMessage(message.chat_id, message.message_id)
            else:
                sendMessage(message.chat_id, 'Ви не зареєстровані. Використовуйте команду /start')

    return "OK"


def set_webhook_logic(request):
    parseResult = urlparse(request.base_url)
    url = "https://" + parseResult.hostname + "/" + current_app.config['TELEGRAM_TOKEN']
    return setupWebhook(url)