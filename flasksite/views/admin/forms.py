from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectField
from flasksite.models import Users


class SendMessageForm(FlaskForm):
    user = QuerySelectField('Користувач', validators=[DataRequired()], query_factory=lambda: Users.query.filter(Users.is_superuser != True), get_label='username')
    text = TextAreaField('Текст', validators=[DataRequired(), Length(max=4096)])
    submit = SubmitField('Відправити')


class SendDocumentForm(FlaskForm):
    user = QuerySelectField('Користувач', validators=[DataRequired()], query_factory=lambda: Users.query.filter(Users.is_superuser != True), get_label='username')
    document = SelectField('Документ', validators=[DataRequired()], choices=[])
    submit = SubmitField('Відправити')