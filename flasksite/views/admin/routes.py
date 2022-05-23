from flasksite import db
from flasksite.models import *
from flasksite.views.admin.controllers.admin_logic import MyModelView, MyFileAdmin
from flask_admin.menu import MenuLink
import os


def admin_routes(admin, app):
    admin.add_view(MyModelView(Users, db.session, name='Користувачі'))
    admin.add_view(MyModelView(Calendars, db.session, name='Календарі'))
    admin.add_view(MyModelView(Events, db.session, name='Події'))
    admin.add_view(MyFileAdmin(os.path.join(os.getcwd(), 'flasksite', 'static', 'uploads'), '/static/uploads/', name='Документи'))
    admin.add_link(MenuLink(name='BotWebhook', url='/' + app.config['TELEGRAM_TOKEN'] + '/setWebhook'))
    admin.add_link(MenuLink(name='Вихід', url='/logout'))