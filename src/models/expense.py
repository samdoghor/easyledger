"""
The model represents an expense entity with attributes such as amount, date,
and a foreign key referencing the expense type. It is associated with expense
types through a many-to-one relationship.
"""

# imports

from datetime import datetime

from . import db


class Expense(db.Model):

    """
    Expense model class representing the 'expenses' table in the database.
    """

    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float(), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,
        nullable=True)

    # foreign keys

    expense_type_id = db.Column(db.Integer, db.ForeignKey(
        'expense_types.id'), nullable=False)

    # relationships

    expense_types = db.relationship('ExpenseType', backref='expenses')
