from flask import Blueprint, request, current_app
from urllib.parse import urlparse
from flasksite.views.bot.controllers.bot_control import setupWebhook, sendMessage


bot = Blueprint('bot', __name__)


@bot.route('/' + current_app.config['TELEGRAM_TOKEN'], methods=['GET', 'POST'])
def home():
    print(request.json['message'])
    return "OK"


@bot.route('/setWebhook', methods=['GET', 'POST'])
def setWebhook():
    parseResult = urlparse(request.base_url)
    url = "https://" + parseResult.hostname + "/" + current_app.config['TELEGRAM_TOKEN']
    return setupWebhook(url)