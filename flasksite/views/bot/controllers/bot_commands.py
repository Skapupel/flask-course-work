import secrets
import string
from flasksite.extensions import db, bcrypt
from flasksite.models import *
from flasksite.views.bot.controllers.telegram_api_functions import sendMessage
from flasksite.views.bot.controllers.messages_text import TEXT


def start(chat_id, username):
    if username:
        if not Users.query.filter_by(username=username).first():
            password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = Users(username, hashed_password, chat_id)
            db.session.add(user)
            db.session.commit()
        sendMessage(chat_id, TEXT['start_with_username'])
    else:
        sendMessage(chat_id, TEXT['start_without_username'])