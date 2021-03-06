from flasksite.extensions import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    chat_id = db.Column(db.Integer, unique=True, nullable=False)
    menu = db.Column(db.String(64), nullable=False, default='menu')
    is_superuser = db.Column(db.Boolean, default=False)
    calendar = db.relationship('Calendars', backref='user', uselist=False, cascade="all, delete", lazy=True)

    def __init__(self, username, password, chat_id, menu='menu', is_superuser=False):
        self.username = username
        self.password = password
        self.chat_id = chat_id
        self.menu = menu
        self.is_superuser = is_superuser

    def __repr__(self):
        return f'<User {self.username}>'