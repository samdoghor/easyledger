"""
The model represents an income entity with attributes such as amount, date,
and a foreign key referencing the income type. It is associated with income
types through a many-to-one relationship.
"""

# imports

from datetime import datetime

from . import db


class Income(db.Model):

    """
    Income model class representing the 'incomes' table in the database.
    """

    __tablename__ = 'incomes'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float(), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,
        nullable=True)

    # foreign keys

    income_type_id = db.Column(db.Integer, db.ForeignKey(
        'income_types.id'), nullable=False)

    # relationships

    income_types = db.relationship('IncomeType', backref='incomes')
