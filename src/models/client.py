"""
Module: ClientModel

Module summary: This module represents the Client model class, which corresponds to the 'clients' table in the database. It defines the structure and attributes of a client entity, including their name, address, email address, and phone number. The Client model also includes timestamps for creation and update dates.

The Client model has a foreign key relationship with the Service model, as indicated by the "service_id" attribute. This relationship establishes a link between a client and the service they are associated with.

Additionally, the Client model has a one-to-many relationship with the ContactPerson model through the "contact_persons" attribute. This relationship allows a client to have multiple contact persons associated with them.

Furthermore, the Client model has a one-to-many relationship with the Job model through the "job_invoices" attribute. This relationship indicates that a client can have multiple job invoices associated with them.
"""

# imports

from datetime import datetime

from . import db


class Client(db.Model):

    """
    Client model class representing the 'clients' table in the database.
    """

    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    address = db.Column(db.Text())
    email_address = db.Column(db.String(), unique=True, nullable=False)
    phone_number = db.Column(db.String(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True)

    # foreign keys
    service_id = db.Column(db.Integer, db.ForeignKey(
        "services.id"), nullable=False)

    # relationships
    contact_persons = db.relationship(
        "ContactPerson", backref="clients", lazy=True)

    job_invoices = db.relationship(
        "Job", backref="job_invoices", lazy=True)
