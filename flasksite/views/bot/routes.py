from flask import Blueprint, request, current_app
from flasksite.views.bot.controllers.bot_control import home_logic, set_webhook_logic


bot = Blueprint('bot', __name__)


@bot.route('/' + current_app.config['TELEGRAM_TOKEN'], methods=['GET', 'POST'])
def home():
    return home_logic(request)


@bot.route('/'  + current_app.config['TELEGRAM_TOKEN'] + '/setWebhook', methods=['GET', 'POST'])
def setWebhook():
    return set_webhook_logic(request)