"""
Module: JobStatusModel

Module summary: This module represents the JobStatus model class, which corresponds to the 'jobs_statuses' table in the database. It defines the structure and attributes of a job status entity, including the status name and timestamps for creation and update dates.

The JobStatus model has a foreign key relationship with the Job model, as indicated by the "job_id" attribute. This relationship establishes a link between a job status and the job it is associated with.

"""


# imports
from datetime import datetime

from . import db


class JobStatus(db.Model):

    """
    JobStatus model class representing the 'jobs_statuses' table in the database.
    """

    __tablename__ = 'jobs_statuses'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(), unique=True, nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,  nullable=True)

    # foreign keys
    job_id = db.Column(db.Integer, db.ForeignKey(
        "jobs.id"), nullable=False)
