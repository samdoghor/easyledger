"""
The model represents a job entity with attributes such as amount, contract
number, start and end dates, associated with a client, service, job invoice,
payments, job expenses, and job statuses.
"""

# imports

from datetime import datetime

from . import db


class Job(db.Model):

    """
    Job model class representing the 'jobs' table in the database.
    """

    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    contract_number = db.Column(db.String(), unique=True, nullable=False)

    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow,
                           onupdate=datetime.utcnow,  nullable=True)

    # foreign keys

    client_id = db.Column(db.Integer, db.ForeignKey(
        'clients.id'), nullable=False)

    service_id = db.Column(db.Integer, db.ForeignKey(
        'services.id'), nullable=False)

    job_invoice_id = db.Column(db.Integer, db.ForeignKey(
        'job_invoices.id'), nullable=False)

    jobs_statuse_id = db.Column(db.Integer, db.ForeignKey(
        'jobs_statuses.id'), nullable=False)

    # relationships

    payments = db.relationship('Payment', backref='jobs', lazy=True)

    job_expenses = db.relationship('JobExpense', backref='jobs', lazy=True)

    job_invoices = db.relationship('JobInvoice', backref='jobs', lazy=True)

    jobs_statuses = db.relationship('JobStatus', backref='jobs', lazy=True)
