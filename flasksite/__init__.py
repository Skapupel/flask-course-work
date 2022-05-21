from flask import Flask
from flasksite.config import Config
from flasksite.extensions import db, migrate


def create_app(config_class=Config):
    # App initialization
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize database
    db.init_app(app)

    # Initialize migration
    migrate.init_app(app, db)

    # Load context
    app.app_context().push()

    # Import blueprints
    from flasksite.views.main.routes import main
    from flasksite.views.bot.routes import bot
    from flasksite.views.admin.routes import admin

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(bot)
    app.register_blueprint(admin)

    return app
