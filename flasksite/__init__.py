from flask import Flask
from flasksite.config import Config
from flasksite.extensions import db, migrate, bcrypt, login_manager
from flasksite.views.admin.utilities import create_admin


def create_app(config_class=Config):
    # App initialization
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize database
    db.init_app(app)

    # Initialize migration
    migrate.init_app(app, db)

    # Initialize bcrypt
    bcrypt.init_app(app)

    # Initialize login manager
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    login_manager.login_message_category = 'info'

    # Load context
    app.app_context().push()

    # Create admin user in db
    create_admin()

    # Import blueprints
    from flasksite.views.main.routes import main
    from flasksite.views.bot.routes import bot
    from flasksite.views.admin.routes import admin
    from flasksite.views.user.routes import user

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(bot)
    app.register_blueprint(admin)
    app.register_blueprint(user)

    return app
