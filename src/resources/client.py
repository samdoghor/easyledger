"""
This Resource controls all Client Resources/
Creation of new client
Deletion of new client
Search and Sort of client
Update an existing client information
View all clients
"""


from flask import render_template

from models import Client
from forms import CreateClientForm

# pylint: disable=R0903


class ClientResource:

    """ Client Resources """

    # pylint: disable=E0211

    def client_index():
        """ Client Homepage """

        clients = Client.query.order_by(Client.name.asc()).all()

        return render_template('pages/client/client.html', clients=clients)

    def client_add():
        """ Client Homepage """

        new_client = CreateClientForm()

        return render_template('pages/client/client_add.html',
                               new_client=new_client)
