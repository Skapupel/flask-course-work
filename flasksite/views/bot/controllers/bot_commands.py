import secrets
import string
import re
from flasksite.extensions import db, bcrypt
from flasksite.models import *
from flasksite.views.bot.controllers.telegram_api_functions import sendMessage, sendMessageWithKeyboard, deleteMessage
from flasksite.views.bot.controllers.bot_utilities import createKeyboardButton
from flasksite.views.bot.controllers.messages_text import TEXT


def start(user, message):
    if user:
        user.menu = 'menu'
        db.session.commit()
        sendMessage(message.chat_id, TEXT['start_with_username'])
    else:
        if message.username:
            password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = Users(message.username, hashed_password, message.chat_id)
            db.session.add(user)
            db.session.commit()
            sendMessage(message.chat_id, TEXT['start_with_username_and_password'].format(password))
        else:
            username = f'{message.chat_id}_{Users.query.count()+1}'
            password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = Users(username, hashed_password, message.chat_id)
            db.session.add(user)
            db.session.commit()
            sendMessage(message.chat_id, TEXT['start_without_username_and_password'].format(username, password))


def username(chat_id, user):
    sendMessage(chat_id, 'Ваш логін: ' + user.username + '\n' + 'Напишіть новий логін:')
    user.menu = 'username'
    db.session.commit()


def after_username(user, message):
    text = message.text.strip()
    if not re.fullmatch("^[!-~]*$", text) or len(text) < 4:
        sendMessageWithKeyboard(message.chat_id, TEXT['new_username_invalid'], [createKeyboardButton('Back to start', 'start')])
    elif Users.query.filter_by(username=text).first():
        sendMessageWithKeyboard(message.chat_id, '⚠️Такий логін вже існує⚠️', [createKeyboardButton('Back to start', 'start')])
    else:
        user.username = text
        user.menu = 'menu'
        db.session.commit()
        sendMessage(message.chat_id, 'Ваш новий логін: ' + user.username)


def password(chat_id, user):
    sendMessage(chat_id, 'Напишіть новий пароль:')
    user.menu = 'password'
    db.session.commit()


def after_password(user, message):
    text = message.text.strip()
    if not re.fullmatch("^[!-~]*$", text) or len(text) < 8:
        sendMessageWithKeyboard(message.chat_id, TEXT['new_password_invalid'], [createKeyboardButton('Back to start', 'start')])
    else:
        user.password = bcrypt.generate_password_hash(text).decode('utf-8')
        user.menu = 'menu'
        db.session.commit()
        sendMessage(message.chat_id, 'Ваш новий пароль: ' + text)


def bot_help(chat_id, user, url):
    user.menu = 'menu'
    db.session.commit()
    sendMessage(chat_id, TEXT['help'].format(url))