from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class CarForm(FlaskForm):
    carname = StringField('Car Name',validators=(DataRequired()])
    current_miles = StringFiled('Current Miles', validators=(DataRequired()]))
    submit = SubmitField('Check Miles')
