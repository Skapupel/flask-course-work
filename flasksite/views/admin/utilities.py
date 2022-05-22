from flasksite.models import Users
from flasksite import db


def create_admin():
    try:
        if not Users.query.filter_by(username='admin').first():
            admin = Users('admin', 'admin', 1, True)
            db.session.add(admin)
            db.session.commit()
    except:
        pass