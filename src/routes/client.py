"""
Home
"""

from flask import Blueprint

from resources import ClientResource

client_blueprint = Blueprint("client", __name__)

client_blueprint.route("/clients")(ClientResource.client_index)
client_blueprint.route("/clients/new_client")(ClientResource.client_add)
