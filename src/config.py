# imports

import os

from dotenv import load_dotenv

# configurations

load_dotenv()

# pylint: disable=E501

dbHost = os.getenv('DBHOST')
dbPort = os.getenv('DBPORT')
dbUsername = os.getenv('DBUSERNAME')
dbPassword = os.getenv('DBPASSWORD')
dbName = os.getenv('DBNAME')

DEBUG = True

SQLALCHEMY_DATABASE_URI = f'postgresql://{dbUsername}:{dbPassword}@{dbHost}:{dbPort}/{dbName}'
SQLALCHEMY_MODIFICATIONS_TRACKS = False

appHost = os.getenv('APPHOST')
appPort = os.getenv('APPPORT')

environment = os.getenv('ENVIRONMENT')

secretKey = os.getenv('SECRETKEY')
