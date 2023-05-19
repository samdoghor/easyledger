"""
The model represents a service entity with attributes such as name, service code, and description, associated with jobs through a one-to-many relationship.
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

    # relationships

    jobs = db.relationship(
        'Job', backref='services', lazy=True)
