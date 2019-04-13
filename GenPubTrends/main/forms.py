from wtforms import validators, TextField, DateField, SubmitField, Form, DateTimeField
from flask_wtf import FlaskForm


class SearchForm(Form):
    disease_name = TextField('Disease name:', validators=[validators.DataRequired(message='Invalid format')])
    start_time = DateTimeField("Start time:", validators=[validators.DataRequired(message='Invalid format')],
                           format='%Y/%m/%d')
    end_time = DateTimeField("End time:", validators=[validators.DataRequired(message='Invalid format')], format='%Y/%m/%d')
    submit_field = SubmitField("Submit")

