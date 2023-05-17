# imports
from datetime import datetime

from . import db


class Client(db.Model):

    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    address = db.Column(db.Text())
    email_address = db.Column(db.String(), unique=True, nullable=False)
    phone_number = db.Column(db.String(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True)

    # foreign keys
    service_id = db.Column(db.Integer, db.ForeignKey(
        "services.id"), nullable=False)

    # relationships
    contact_persons = db.relationship(
        "ContactPerson", backref="clients", lazy=True)

    job_invoices = db.relationship(
        "Job", backref="job_invoices", lazy=True)
