""" 
This module defines the resource for the index page
"""


from flask import jsonify, request

# pylint: disable=R0903


class IndexResource:

    """ Index Resources """

    # pylint: disable=E0211

    def index():
        """ Confirms and displays basic info that the server is running """

        server = jsonify({
            "App Name": "Easy Ledger App",
            "Current URL": f"{request.url}",
            "Endpoints Access": "http://127.0.0.1:3303/[endpoints]",
            "Message": "The server is up and running",
            "Version": "1.0.0"
        })

        return server
