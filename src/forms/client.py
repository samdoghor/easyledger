"""
This module defines all forms needed by the clients to create, update, and delete
"""
# imports

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import IntegerField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email

# forms


class CreateClientForm(FlaskForm):
    """ This class is use to create new clients """
    name = StringField('Name', validators=[DataRequired()])
    address = TextAreaField('Address')
    email_address = StringField('Email Address', validators=[Email()])
    phone_number = IntegerField('Phone Number')
    registration_number = StringField('Registration Numeber')
    client_logo = FileField('Logo', validators=[FileAllowed(
        ['jpg', 'png'], 'JPG & PNG Formats Only!')])
