"""
This Resource controls all Client Resources/
Creation of new client
Deletion of client
Search and Sort of client
Update an existing client information
View all clients
View one client
"""


from flask import render_template

from models import Client

# pylint: disable=R0903


class ClientResource:

    """ Client Resources """

    # pylint: disable=E0211

    def client_view_all_grid():
        """ View all client in grid form """

        clients = Client.query.order_by(Client.name.asc()).all()

        return render_template('pages/client/client-grid.html',
                               clients=clients)

    def client_view_all_list():
        """ View all client in grid form """

        clients = Client.query.order_by(Client.name.asc()).all()

        return render_template('pages/client/client-list.html',
                               clients=clients)
