from flasksite.extensions import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_superuser = db.Column(db.Boolean, default=False)
    calendar = db.relationship('Calendars', backref='user', uselist=False, cascade="all, delete", lazy=True)

    def __init__(self, username, password, is_superuser=False):
        self.username = username
        self.password = password
        self.is_superuser = is_superuser

    def __repr__(self):
        return f'<User {self.username}>'