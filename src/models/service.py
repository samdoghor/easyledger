# imports
from datetime import datetime

from . import db


class Service(db.Model):

    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    service_code = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,  nullable=True)

   # foreign keys
    job_id = db.Column(db.Integer, db.ForeignKey(
        "jobs.id"), nullable=False)

    # relationships
    clients = db.relationship(
        "Client", backref="services", lazy=True)
