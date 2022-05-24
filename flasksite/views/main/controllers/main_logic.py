from flask import flash, render_template, redirect, url_for, request
from flask_login import current_user
from flasksite.models import Calendars, Events, Users
from flasksite import db
from flasksite.views.main.forms import AddForm
from datetime import datetime
import threading
import requests
from urllib.parse import urlparse


def send_notification(chat_id, text, url):
    requests.post(url, json={'chat_id': chat_id, 'text': text})
    return


def home_logic():
    if current_user.is_superuser:
        return redirect(url_for('admin.home'))

    calendar = Calendars.query.filter_by(user_id=current_user.id).first()
    if not calendar:
        calendar = Calendars(name=current_user.username, user_id=current_user.id)
        db.session.add(calendar)
        db.session.commit()
    
    events = Events.query.filter_by(calendar_id=calendar.id).all()
    user = Users.query.filter_by(id=current_user.id).first()

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

    for event in events:
        if event.notification and event.time > datetime.now():
            parseResult = urlparse(request.base_url)
            url = "https://" + parseResult.hostname + url_for('api.bot_send_message')
            found = False
            for thing in threading.enumerate():
                if isinstance(thing, threading.Timer):
                    if thing.getName() == event.thread:
                        found = True
                        break
            if not found:
                t = threading.Timer((event.time - datetime.now()).total_seconds(), send_notification, [user.chat_id, event.description, url])
                event.thread = t.getName()
                db.session.commit()
                t.start()
        elif not event.notification and event.time > datetime.now():
            for thing in threading.enumerate():
                if isinstance(thing, threading.Timer):
                    if thing.getName() == event.thread:
                        thing.cancel()
                        event.thread = None
                        db.session.commit()
        elif event.time <= datetime.now():
            db.session.delete(event)
            db.session.commit()
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


def notification_logic(request):
    if request.method == 'POST':
        event = Events.query.filter_by(id=request.form.get('id')).first()
        event.notification = not event.notification
        db.session.commit()
        flash('Подію змінено!', 'success')
        return redirect(url_for('main.home'))
    flash('Не вдалось змінити подію', 'danger')
    return redirect(url_for('main.home'))