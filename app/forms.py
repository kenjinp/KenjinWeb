from flask.ext.wtf import Form
from wtforms import TextAreaField, BooleanField, TextField, SubmitField, PasswordField
from wtforms.validators import Required, Length

class ContactForm(Form):
        name = TextField('Name', validators = [Required()])
        email = TextField('Email', validators = [Required()])
        text = TextAreaField('Text', validators = [Required()])
        submit = SubmitField("Send!")
