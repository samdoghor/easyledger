# imports
from flask_sqlalchemy import SQLAlchemy

# configurations
db = SQLAlchemy()

# moduel imports
from .client import Client
from .contact_person import ContactPerson
from .job import Job
from .job_expense import JobExpense
from .job_invoice import JobInvoice
from .job_status import JobStatus
from .service import Service