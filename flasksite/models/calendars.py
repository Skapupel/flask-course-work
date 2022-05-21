from flasksite.extensions import db


class Calendars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    events = db.relationship('Events', backref='calendar', cascade="all, delete", lazy=True)

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f'<Calendar {self.name}>'