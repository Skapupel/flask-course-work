from flask import render_template, redirect, url_for
from flask_login import current_user


def home_logic():
    if current_user.is_superuser:
        return redirect(url_for('admin.home'))
    return render_template('home.html')