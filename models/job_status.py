# imports
from datetime import datetime

from . import db

class JobStatus(db.Model):

    __tablename__ = 'jobs_statuses'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(), unique=True, nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=True)
    
    # foreign keys
    job_id = db.Column(db.Integer, db.ForeignKey(
        "jobs.id"), nullable=False)
