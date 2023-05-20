"""
The model represents a client entity with attributes such as name,
address,contact information, and registration details, associated with contact
persons and jobs.
"""

# imports

from datetime import datetime

from . import db

# pylint: disable=R0903


class Client(db.Model):

    """
    Client model class representing the 'clients' table in the database.
    """

    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    address = db.Column(db.Text())
    email_address = db.Column(db.String(), unique=True, nullable=True)
    phone_number = db.Column(db.String(), nullable=True)
    registration_number = db.Column(db.String(), unique=True, nullable=True)
    client_logo = db.Column(db.String(), nullable=True)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,
        nullable=True
    )

    # relationships

    contact_persons = db.relationship(
        "ContactPerson", backref="clients", lazy=True)

    jobs = db.relationship("Job", backref="clients", lazy=True)
