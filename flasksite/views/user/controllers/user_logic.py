import flasksite.views.user.controllers.login_manage
from flasksite.views.user.forms import LoginForm
from flasksite.models import Users
from flasksite import bcrypt
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user


def login_logic(request):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash(f'Ви увійшли як {form.username.data}.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Невірний логін або пароль.', 'danger')
    return render_template('login.html', title='Login', form=form)


def logout_logic():
    logout_user()
    return redirect(url_for('user.login'))