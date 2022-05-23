from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_login import current_user
from flask import redirect, url_for, flash, request
from flasksite.views.admin.forms import SendMessageForm, SendDocumentForm
from flasksite.views.bot.controllers.telegram_api_functions import sendMessage, sendDocument
from urllib.parse import urlparse


class HomeView(AdminIndexView):
    @expose('/', methods=['GET', 'POST'])
    def home(self):
        send_message_form = SendMessageForm()
        send_document_form = SendDocumentForm()
        if send_message_form.validate_on_submit():
            user = send_message_form.user.data
            text = send_message_form.text.data
            if sendMessage(user.chat_id, text):
                flash('Повідомлення відправлено', 'success')
            else:
                flash('Помилка відправлення повідомлення', 'danger')
        
        if send_document_form.validate_on_submit():
            user = send_document_form.user.data
            parseResult = urlparse(request.base_url)
            document = send_document_form.document.data
            url = "https://" + parseResult.hostname + '/static/uploads/' + document
            if sendDocument(user.chat_id, url):
                flash('Документ відправлено', 'success')
            else:
                flash('Помилка відправлення документа', 'danger')

        return self.render('admin.html', title='Admin', send_message_form=send_message_form, send_document_form=send_document_form)

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_superuser

    def inaccessible_callback(self, name, **kwargs):
        flash('Ви не маєте доступу до цієї сторінки', 'warning')
        return redirect(url_for('main.home'))


class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_superuser

    def inaccessible_callback(self, name, **kwargs):
        flash('Ви не маєте доступу до цієї сторінки', 'warning')
        return redirect(url_for('main.home'))


class MyFileAdmin(FileAdmin):

    allowed_extensions=['pdf']

    column_labels = {
        'name': 'Назва',
        'size': 'Розмір',
        'date': 'Дата'
    }

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_superuser

    def inaccessible_callback(self, name, **kwargs):
        flash('Ви не маєте доступу до цієї сторінки', 'warning')
        return redirect(url_for('main.home'))

        