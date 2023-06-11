# imports

from flask import Blueprint, Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

import config
import routes
from models import db

# configurations

# pylint: disable=E501

server = Flask(__name__)

server.config['SECRET_KEY'] = config.secretKey

server.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
server.config['SQLALCHEMY_MODIFICATIONS_TRACKS'] = config.SQLALCHEMY_MODIFICATIONS_TRACKS

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
