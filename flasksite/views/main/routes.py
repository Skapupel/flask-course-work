from flask import Blueprint
from flask_login import login_required
from flasksite.views.main.controllers.main_logic import home_logic


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return home_logic()