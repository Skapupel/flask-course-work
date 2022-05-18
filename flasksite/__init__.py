from flask import Flask
from utilities.env import get_from_env


app = Flask(__name__)
app.config['SECRET_KEY'] = get_from_env('SECRET_KEY')
app.config['TELEGRAM_TOKEN'] = get_from_env('TELEGRAM_TOKEN')


from flasksite import routes
from bot import bot_routes