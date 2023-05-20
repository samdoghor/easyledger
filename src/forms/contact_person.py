"""
This module defines all forms needed by the contact persons 
"""
# imports

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Email

# forms


class CreateContactPersonForm(FlaskForm):

    """ This class is use to create new contact persons """

    full_name = StringField('Full Name', validators=[DataRequired()])
    email_address = StringField('Email Address', validators=[Email()])
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Add New Client')
