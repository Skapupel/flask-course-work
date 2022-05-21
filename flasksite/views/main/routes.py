from flask import Blueprint, render_template, url_for, current_app


main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')