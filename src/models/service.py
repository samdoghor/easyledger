"""
Module: ServiceModel

Module summary: This module represents the Service model class, which corresponds to the 'services' table in the database. It defines the structure and attributes of a service entity, including the name, service code, description, and timestamps for creation and update dates.

The Service model has a foreign key relationship with the Job model, as indicated by the "job_id" attribute. This relationship establishes a link between a service and the job it is associated with.

Additionally, the Service model has a one-to-many relationship with the Client model through the "clients" attribute. This relationship indicates that a service can be associated with multiple clients.
"""


# imports
from datetime import datetime

from . import db


class Service(db.Model):

    """
    Service model class representing the 'services' table in the database.
    """

    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    service_code = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,  nullable=True)

   # foreign keys
    job_id = db.Column(db.Integer, db.ForeignKey(
        "jobs.id"), nullable=False)

    # relationships
    clients = db.relationship(
        "Client", backref="services", lazy=True)
