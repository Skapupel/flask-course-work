from flask import flash, render_template, redirect, url_for
from flask_login import current_user
from flasksite.models import Calendars, Events
from flasksite import db
from flasksite.views.main.forms import AddForm
from datetime import datetime


def home_logic():
    if current_user.is_superuser:
        return redirect(url_for('admin.home'))

    calendar = Calendars.query.filter_by(user_id=current_user.id).first()
    if not calendar:
        calendar = Calendars(name=current_user.username, user_id=current_user.id)
        db.session.add(calendar)
        db.session.commit()
    
    events = Events.query.filter_by(calendar_id=calendar.id).all()

    form = AddForm()

    if form.validate_on_submit():
        if form.time.data <= datetime.now():
            flash('Вкажіть майбутню дату!', 'danger')
            return redirect(url_for('main.home'))
        event = Events(title=form.name.data, description=form.description.data, time=form.time.data, calendar_id=calendar.id)
        db.session.add(event)
        db.session.commit()
        flash('Подію додано!', 'success')
        return redirect(url_for('main.home'))

    return render_template('home.html', events=events, form=form)


def delete_logic(request):
    if request.method == 'POST':
        event = Events.query.filter_by(id=request.form.get('id')).first()
        db.session.delete(event)
        db.session.commit()
        flash('Подію видалено!', 'success')
        return redirect(url_for('main.home'))
    flash('Не вдалось видалити подію', 'danger')
    return redirect(url_for('main.home'))