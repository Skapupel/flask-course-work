from flasksite.views.bot.controllers.telegram_api_functions import sendMessage


def home_logic():
    return {'status': 'OK'}


def bot_send_message_logic(request):
    if request.method == 'POST':
        json = request.json
        if json:
            sendMessage(json['chat_id'], json['text'])
            return {'status': 'OK', 'success': True}
        else:
            return {'status': 'ERROR', 'success': False}
    return {'status': 'OK'}