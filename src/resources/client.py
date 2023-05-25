"""
the
"""


from flask import render_template

from models import Client

# pylint: disable=R0903


class ClientResource:

    """ Client Resources """

    # pylint: disable=E0211

    def client_index():
        """ Client Homepage """

        clients = Client.query.order_by(Client.name.asc()).all()

        return render_template('pages/client.html', clients=clients)
