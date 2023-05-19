"""
The model represents a payment entity with attributes such as amount and date, associated with a job through a foreign key reference.
"""

# imports

from datetime import datetime

from . import db


class Payment(db.Model):

    """
    Payment model class representing the 'payments' table in the database.
    """

    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float(), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow,
                           onupdate=datetime.utcnow, nullable=True)

    # foreign keys

    job_id = db.Column(db.Integer, db.ForeignKey(
        'job.id'), nullable=False)
