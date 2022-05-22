from flask import Blueprint, render_template, url_for, current_app
from flask_login import login_required


main = Blueprint('main', __name__)


@main.route('/')
@login_required
def home():
    return render_template('home.html')