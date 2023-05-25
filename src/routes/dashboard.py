"""
Home
"""

from flask import Blueprint

from resources import DashboardResource

dashboard_blueprint = Blueprint("dashboard", __name__)

dashboard_blueprint.route("/dashboard")(DashboardResource.dashboard_index)
