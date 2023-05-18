"""
Module: JobModel

Module summary: This module represents the Job model class, which corresponds to the 'jobs' table in the database. It defines the structure and attributes of a job entity, including the amount, start date, end date, and timestamps for creation and update dates.

The Job model has a foreign key relationship with the JobInvoice model, as indicated by the "job_invoice_id" attribute. This relationship establishes a link between a job and the job invoice it is associated with.

Additionally, the Job model has one-to-many relationships with the JobStatus, JobExpense, and Service models through the "job_statuses", "job_expenses", and "services" attributes, respectively. These relationships indicate that a job can have multiple job statuses, job expenses, and services associated with it.
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

    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,  nullable=True)

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
