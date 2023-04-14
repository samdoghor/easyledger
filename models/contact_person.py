# imports
from datetime import datetime

from . import db


class ContactPerson(db.Model):

    __tablename__ = 'contact_persons'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(), nullable=False)
    email_address = db.Column(db.String(), unique=True, nullable=False)
    phone_number = db.Column(db.String(), nullable=False)
    
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=True)

    # foreign keys
    client_id = db.Column(db.Integer, db.ForeignKey(
        "clients.id"), nullable=False)
