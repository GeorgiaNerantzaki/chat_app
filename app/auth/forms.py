from flask_wtf import Form
from wtforms import StringField, PasswordField,validators
from wtforms.validators import Email, DataRequired

class LoginForm(Form):
    email = StringField('Email', id = 'email', validators = [DataRequired(), validators.Email()])
    password = PasswordField('Password', id = 'password_login', validators = [DataRequired()])

class RegisterForm(Form):
    password = StringField('Password', id = 'password_register', validators = [DataRequired()])
    email = StringField('Email', id = 'email_register', validators = [DataRequired()])
    confirm_password = StringField('Confirm Password', id = 'password_confirm', validators = [DataRequired()])
    first_name = StringField('First Name', id = 'first_name', validators = [DataRequired()])
    last_name = StringField('Last Name', id = 'last_name', validators = [DataRequired()])
    username = StringField('Username', id = 'username', validators = [DataRequired()])
    