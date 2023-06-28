"""
Home
"""

from flask import Blueprint

from resources import ClientResource

client_blueprint = Blueprint("client", __name__)

client_blueprint.route("/clients-grid")(ClientResource.client_view_all_grid)
client_blueprint.route("/clients-list")(ClientResource.client_view_all_list)
