"""
The model represents an expense type entity with attributes such as expense
type name and description, associated with expenses through a many-to-one
relationship.
"""

# imports

from datetime import datetime

from . import db


class ExpenseType(db.Model):

    """
    ExpenseType model class representing the 'expense_types' table in the
    database.
    """

    __tablename__ = 'expense_types'

    id = db.Column(db.Integer, primary_key=True)
    expense_type = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String(), nullable=True)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow,
                           onupdate=datetime.utcnow, nullable=True)
