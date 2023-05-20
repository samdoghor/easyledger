""" 
the
"""


from flask import render_template

# pylint: disable=R0903


class ClientResource:

    """ Client Resources """

    # pylint: disable=E0211

    def client_index():
        """ Client Hoempage """

        return render_template('pages/client.html')
