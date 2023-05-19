"""
The model represents a contact person associated with a client, having attributes such as full name, email address, and phone number, with a foreign key referencing the client they belong to.
"""

# imports

from datetime import datetime

from . import db


class ContactPerson(db.Model):

    """
    ContactPerson model class representing the 'contact_persons' table in the database.
    """

    __tablename__ = 'contact_persons'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(), nullable=False)
    email_address = db.Column(db.String(), unique=True, nullable=True)
    phone_number = db.Column(db.String(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True)

    # foreign keys

    client_id = db.Column(db.Integer, db.ForeignKey(
        'clients.id'), nullable=False)
