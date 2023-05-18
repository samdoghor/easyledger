"""
Module: JobInvoiceModel

Module summary: This module represents the JobInvoice model class, which corresponds to the 'job_invoices' table in the database. It defines the structure and attributes of a job invoice entity, including the invoice number, issued date, invoice link, and timestamps for creation and update dates.

The JobInvoice model has a foreign key relationship with the Client model, as indicated by the "client_id" attribute. This relationship establishes a link between a job invoice and the client it is associated with.

Additionally, the JobInvoice model has a one-to-many relationship with the Job model through the "jobs" attribute. This relationship indicates that a job invoice can have multiple jobs associated with it.

Furthermore, the JobInvoice model has a one-to-many relationship with the JobExpense model through the "job_expenses" attribute. This relationship indicates that a job invoice can have multiple job expenses associated with it.
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
    client_id = db.Column(db.Integer, db.ForeignKey(
        "clients.id"), nullable=False)

    # relationships
    jobs = db.relationship(
        "Job", backref="job_invoices", lazy=True)
    job_expenses = db.relationship(
        "JobExpense", backref="jobs", lazy=True)
