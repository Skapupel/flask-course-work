from flasksite.extensions import db


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=True)
    time = db.Column(db.DateTime, nullable=False)
    calendar_id = db.Column(db.Integer, db.ForeignKey('calendars.id'), nullable=False)

    def __init__(self, title, description, time, calendar_id):
        self.title = title
        self.description = description
        self.time = time
        self.calendar_id = calendar_id

    def __repr__(self):
        return f'<UserEvent {self.title}>, {self.time}'