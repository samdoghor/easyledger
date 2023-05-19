"""
The model represents an income type entity with attributes such as income type name and description, associated with incomes through a many-to-one relationship.
"""

# imports

from datetime import datetime

from . import db


class IncomeType(db.Model):

    """
    IncomeType model class representing the 'income_types' table in the database.
    """

    __tablename__ = 'income_types'

    id = db.Column(db.Integer, primary_key=True)
    income_type = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String(), nullable=True)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow,
                           onupdate=datetime.utcnow, nullable=True)
