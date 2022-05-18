from urllib.parse import urlparse
from flask import request
from bot.bot_control import setupWebhook, sendMessage
from flasksite import app


@app.route('/' + app.config['TELEGRAM_TOKEN'], methods=['GET', 'POST'])
def bot():
    print(request.json['message'])
    return "OK"


@app.route('/setWebhook', methods=['GET', 'POST'])
def setWebhook():
    o = urlparse(request.base_url)
    url = "https://" + o.hostname + "/" + app.config['TELEGRAM_TOKEN']
    return setupWebhook(url)