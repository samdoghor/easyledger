"""
the
"""


from flask import render_template

# pylint: disable=R0903


class DashboardResource:

    """ Dashboard Resources """

    # pylint: disable=E0211

    def dashboard_index():
        """ Dashboard Hoempage """

        return render_template('pages/dashboard.html')
