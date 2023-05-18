"""
Module: ContactPersonModel

Module summary: This module represents the ContactPerson model class, which corresponds to the 'contact_persons' table in the database. It defines the structure and attributes of a contact person entity associated with a client.

The ContactPerson model has a foreign key relationship with the Client model, as indicated by the "client_id" attribute. This relationship establishes a link between a contact person and the client they are associated with.

Overall, this module defines the ContactPerson model class and its relationship with the Client model, providing the necessary structure for working with contact person data in the database.
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
    email_address = db.Column(db.String(), unique=True, nullable=False)
    phone_number = db.Column(db.String(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True)

    # foreign keys
    client_id = db.Column(db.Integer, db.ForeignKey(
        "clients.id"), nullable=False)
