from flasksite.models import Users
from flasksite import db, bcrypt


def create_admin():
    try:
        if not Users.query.filter_by(username='admin').first():
            password = 'admin'
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            admin = Users('admin', hashed_password, 1, is_superuser=True)
            db.session.add(admin)
            db.session.commit()
    except:
        pass