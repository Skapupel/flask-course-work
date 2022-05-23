from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()


migrate = Migrate()


bcrypt = Bcrypt()


login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message = "Ваш потрібно увійти щоб мати доступ до цієї сторінки"
login_manager.login_message_category = 'info'