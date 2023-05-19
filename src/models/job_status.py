"""
The model represents a job status entity with attributes such as status, associated with jobs through a many-to-one relationship.
"""

# imports

from datetime import datetime

from . import db


class JobStatus(db.Model):

    """
    JobStatus model class representing the 'jobs_statuses' table in the database.
    """

    __tablename__ = 'jobs_statuses'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(), unique=True, nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,  nullable=True)
