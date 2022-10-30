from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SearchField
from wtforms.validators import DataRequired, EqualTo

#recently added first and last name. checked for functionality? y/n< >evan

class UserCreationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    first_name = StringField('First Name',validators=[DataRequired()])
    last_name = StringField('Last Name',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

class UserLoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ItemForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    submit = SubmitField()



