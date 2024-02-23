# pylint: disable=unused-argument
"""Custom error pages"""

from flask import render_template


def forbidden(e):
    """403 Forbidden"""
    return render_template('errors/403.jinja2', title='Forbidden'), 403


def page_not_found(e):
    """404 Page Not Found"""
    return render_template('errors/404.jinja2', title='Page Not Found'), 404


def internal_server_error(e):
    """500 Internal Server Error"""
    return render_template('errors/500.jinja2', title='Internal Server Error'), 500
