from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length


class AddForm(FlaskForm):
    name = StringField('Назва події', validators=[DataRequired(), Length(min=4, max=64)])
    description = TextAreaField('Опис події', validators=[DataRequired(), Length(min=4, max=1024)])
    time = DateTimeField('Час події', validators=[DataRequired()])
    submit = SubmitField('Додати')