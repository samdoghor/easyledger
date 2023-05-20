"""
The model represents a job expense entity with attributes such as amount and
description, associated with a job through a foreign key reference.
"""

# imports

from datetime import datetime

from . import db


class JobExpense(db.Model):

    """
    JobExpense model class representing the 'job_expenses' table in the
    database.
    """

    __tablename__ = 'job_expenses'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,
        nullable=True)

    # foreign keys

    job_id = db.Column(db.Integer, db.ForeignKey(
        'jobs.id'), nullable=False)
