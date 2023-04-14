# imports
from flask import Flask
from flask_migrate import Migrate

import config
from models import db

# configurations
server = Flask(__name__)

server.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
server.config['SQLALCHEMY_MODIFICATIONS_TRACKS'] = config.SQLALCHEMY_MODIFICATIONS_TRACKS

db.init_app(server)
db.app = (server)
migrate = Migrate(server, db)

# application run
if __name__ == "__main__":
    server.debug = config.DEBUG
    server.run()
