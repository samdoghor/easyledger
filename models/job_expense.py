# imports
from datetime import datetime

from . import db

class JobExpense(db.Model):

    __tablename__ = 'job_expenses'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=True)
    
   # foreign keys
    job_id = db.Column(db.Integer, db.ForeignKey(
        "jobs.id"), nullable=False)
    
    job_invoice_id = db.Column(db.Integer, db.ForeignKey(
        "job_invoices.id"), nullable=False)
