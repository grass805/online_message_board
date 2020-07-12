'''
#4 step
forums: fields that users can submit
'''

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class submitForum(FlaskForm):
    name = StringField('Enter User Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Leave a Message', validators=[DataRequired(), Length(1, 100)])
    submit = SubmitField()