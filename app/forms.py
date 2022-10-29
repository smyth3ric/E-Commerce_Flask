from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SearchField
from wtforms.validators import DataRequired, EqualTo



class UserCreationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    first_name = StringField('First Name',validators=[DataRequired()])#recently added whole page. checked for functionality? y/n< >evan
    last_name = StringField('Last Name',validators=[DataRequired()])#recently added whole page. checked for functionality? y/n< >evan
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('SUBMIT')

class UserLoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')




