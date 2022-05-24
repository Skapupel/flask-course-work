from flask import Blueprint, request
from flask_login import login_required
from flasksite.views.main.controllers.main_logic import home_logic, delete_logic, notification_logic


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return home_logic()


@main.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    return delete_logic(request)


@main.route('/notification', methods=['GET', 'POST'])
@login_required
def notification():
    return notification_logic(request)