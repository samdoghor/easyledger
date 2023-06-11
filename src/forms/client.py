"""
This module defines all forms needed by the clients
"""
# imports

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired

# forms


class CreateClientForm(FlaskForm):

    """ This class is use to create new clients """

    name = StringField('Name', validators=[DataRequired()])
    email_address = StringField('Email Address')
    phone_number = IntegerField('Phone Number')
    registration_number = StringField('Registration Number')
    street_name = StringField('Street Name')
    city = StringField('City')
    state = StringField('State')
    country = StringField('Country')
    zipcode = StringField('Zipcode')
    client_logo = FileField('Logo', validators=[FileAllowed(
        ['jpg', 'png'], 'JPG & PNG Formats Only!')])
    submit = SubmitField('Add New Client')
