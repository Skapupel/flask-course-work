import secrets
import string
import re
from flasksite.extensions import db, bcrypt
from flasksite.models import *
from flasksite.views.bot.controllers.telegram_api_functions import sendMessage
from flasksite.views.bot.controllers.messages_text import TEXT


def start(chat_id, username):
    if username:
        if not Users.query.filter_by(chat_id=chat_id).first():
            password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = Users(username, hashed_password, chat_id)
            db.session.add(user)
            db.session.commit()
            sendMessage(chat_id, TEXT['start_with_username_and_password'].format(password))
        else:
            sendMessage(chat_id, TEXT['start_with_username'])
    else:
        if not Users.query.filter_by(chat_id=chat_id).first():
            username = f'{chat_id}_{Users.query.count()+1}'
            password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = Users(username, hashed_password, chat_id)
            db.session.add(user)
            db.session.commit()
            sendMessage(chat_id, TEXT['start_without_username_and_password'].format(username, password))
        else:
            sendMessage(chat_id, TEXT['start_with_username'])


def username(chat_id):
    user = Users.query.filter_by(chat_id=chat_id).first()
    sendMessage(chat_id, 'Ваш логін: ' + user.username + '\n' + 'Напишіть новий логін:')
    user.menu = 'username'
    db.session.commit()


def after_username(user, message):
    text = message.text.strip()
    if not re.fullmatch("^[!-~]*$", text):
        sendMessage(message.chat_id, '⚠️Використовуйте латинські літери, цифри та знаки пунктуації.\n⚠️Логін не може містити пробіли.')
    elif Users.query.filter_by(username=text).first():
        sendMessage(message.chat_id, '⚠️Такий логін вже існує⚠️')
    else:
        user.username = text
        user.menu = 'menu'
        db.session.commit()
        sendMessage(message.chat_id, 'Ваш новий логін: ' + user.username)
