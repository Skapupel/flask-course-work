from utilities.env import get_from_env


class Config:
    SECRET_KEY = get_from_env('SECRET_KEY')
    TELEGRAM_TOKEN = get_from_env('TELEGRAM_TOKEN')
    SQLALCHEMY_DATABASE_URI = get_from_env('DATABASE_URI')
    FLASK_ADMIN_SWATCH = 'Cerulean'