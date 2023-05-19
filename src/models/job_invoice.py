"""
The model represents a job invoice entity with attributes such as invoice number, issued date, invoice link, associated with a job through a foreign key reference.
"""

# imports

from datetime import datetime

from . import db


class JobInvoice(db.Model):

    """
    JobInvoice model class representing the 'job_invoices' table in the database.
    """

    __tablename__ = 'job_invoices'

    id = db.Column(db.Integer, primary_key=True)
    invoice_no = db.Column(db.String(), unique=True, nullable=False)
    issued_on = db.Column(db.DateTime(), nullable=False)
    invoice_link = db.Column(db.String(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,  nullable=True)

    # foreign keys

    job_id = db.Column(db.Integer, db.ForeignKey(
        'jobs.id'), nullable=False)
