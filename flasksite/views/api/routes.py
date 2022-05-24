from flask import Blueprint, request
from flasksite.views.api.controllers.api_logic import home_logic, bot_send_message_logic


api = Blueprint('api', __name__)


@api.route('/api', methods=['GET', 'POST'])
def home():
    return home_logic()


@api.route('/api/botSendMessage', methods=['GET', 'POST'])
def bot_send_message():
    return bot_send_message_logic(request)