# imports
from flask import Blueprint, Flask
from flask_migrate import Migrate

import config
import routes
from models import db

# configurations
server = Flask(__name__)

server.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
server.config['SQLALCHEMY_MODIFICATIONS_TRACKS'] = config.SQLALCHEMY_MODIFICATIONS_TRACKS

db.init_app(server)
db.app = (server)
migrate = Migrate(server, db)

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint)

# errors handling

# application run
if __name__ == "__main__":
    server.debug = config.DEBUG
    server.run()
