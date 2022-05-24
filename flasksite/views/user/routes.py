from flask import Blueprint, request
from flasksite.views.user.controllers.user_logic import login_logic, logout_logic


user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login():
    return login_logic(request)


@user.route('/logout')
def logout():
    return logout_logic()