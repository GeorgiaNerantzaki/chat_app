from flask_wtf import Form, FlaskForm
from wtforms import StringField,validators, SubmitField,HiddenField
from wtforms.validators import Email, DataRequired

class AddContactForm(FlaskForm):
    contact_email = StringField('Email', id  = "contact_email",validators = [DataRequired(), validators.Email()])
    submit  = SubmitField('Find Contact')
    
class CreateChatForm(FlaskForm):
    createchat = HiddenField('Contact ID', validators = [DataRequired()])
    submit = SubmitField('Create Chat')
    
class MessageForm(FlaskForm):
    message_text = StringField('Send a new Message',id = "message_text", validators = [DataRequired()])
    submit = SubmitField('Send Message')
    

