# imports
from datetime import datetime

from . import db

class Job(db.Model):

    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)

    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=True)
    
   # foreign keys
    job_invoice_id = db.Column(db.Integer, db.ForeignKey(
        "job_invoices.id"), nullable=False)
    
    # relationships
    job_statuses = db.relationship(
        "JobStatus", backref="jobs", lazy=True)
    job_expenses = db.relationship(
        "JobExpense", backref="jobs", lazy=True)
    services = db.relationship(
        "Service", backref="jobs", lazy=True)
