from flask import Flask
from utilities.env import get_from_env


app = Flask(__name__)
app.config['SECRET_KEY'] = get_from_env('SECRET_KEY')


from flasksite import routes