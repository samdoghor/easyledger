
"""
Module: JobExpenseModel

Module summary: This module represents the JobExpense model class, which corresponds to the 'job_expenses' table in the database. It defines the structure and attributes of a job expense entity, including the amount, description, and timestamps for creation and update dates.

The JobExpense model has foreign key relationships with the Job and JobInvoice models, as indicated by the "job_id" and "job_invoice_id" attributes. These relationships establish links between a job expense and the job and job invoice they are associated with, respectively.
"""

# imports
from datetime import datetime

from . import db


class JobExpense(db.Model):

    """
    JobExpense model class representing the 'job_expenses' table in the database.
    """

    __tablename__ = 'job_expenses'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,  nullable=True)

   # foreign keys
    job_id = db.Column(db.Integer, db.ForeignKey(
        "jobs.id"), nullable=False)

    job_invoice_id = db.Column(db.Integer, db.ForeignKey(
        "job_invoices.id"), nullable=False)
