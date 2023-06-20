"""
This module defines the server configuration required to run the app
successfully.

# Configuration defined
Server as Flask APP
Flask Blueprint
Flask SQLAlchemy for DB
Flask Migrate for DB-ORM
CSRF Protection
Error Handling
"""

# imports


from flask import Blueprint, Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

import config
import routes
from models import db

# configurations


server = Flask(__name__)

server.config['SECRET_KEY'] = config.secretKey

server.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
server.config['SQLALCHEMY_MODIFICATIONS_TRACKS'] = config.SQLALCHEMY_MODIFICATIONS_TRACKS  # noqa

db.init_app(server)
db.app = (server)
migrate = Migrate(server, db)
WTF_CSRF_SECRET_KEY = config.secretKey
csrf = CSRFProtect(server)


for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint)

# errors handling

# application run

if __name__ == "__main__":
    server.debug = config.DEBUG
    server.run()
