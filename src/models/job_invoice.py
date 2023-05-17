# imports
from datetime import datetime

from . import db


class JobInvoice(db.Model):

    __tablename__ = 'job_invoices'

    id = db.Column(db.Integer, primary_key=True)
    invoice_no = db.Column(db.String(), unique=True, nullable=False)
    issued_on = db.Column(db.DateTime(), nullable=False)
    invoice_link = db.Column(db.String(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,  nullable=True)

    # foreign keys
    client_id = db.Column(db.Integer, db.ForeignKey(
        "clients.id"), nullable=False)

    # relationships
    jobs = db.relationship(
        "Job", backref="job_invoices", lazy=True)
    job_expenses = db.relationship(
        "JobExpense", backref="jobs", lazy=True)
