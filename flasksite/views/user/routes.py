from flask import Blueprint
from flasksite.views.user.controllers.user_logic import login_logic


user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login():
    return login_logic()