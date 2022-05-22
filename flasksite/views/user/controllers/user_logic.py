from flasksite.views.user.forms import LoginForm
from flasksite.models import Users
from flasksite import bcrypt
from flask import render_template, flash, redirect, url_for
from flask_login import login_user
import flasksite.views.user.controllers.login_manage


def login_logic():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash(f'Ви увійшли як {form.username.data}.', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Невірний логін або пароль.', 'danger')
    return render_template('login.html', title='Login', form=form)