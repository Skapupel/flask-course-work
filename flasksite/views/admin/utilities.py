from flasksite.models import Users
from flasksite import db, bcrypt
from utilities.env import get_from_env


def create_admin():
    try:
        if not Users.query.filter_by(username='admin').first():
            password = get_from_env('ADMIN_PASSWORD')
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            admin = Users('admin', hashed_password, 1, is_superuser=True)
            db.session.add(admin)
            db.session.commit()
    except:
        pass