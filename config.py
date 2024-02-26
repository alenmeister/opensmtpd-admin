"""Application config"""

from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, '.env'))

SQLITE_DB = 'sqlite:///' + path.join(BASE_DIR, 'opensmtpd.db')


class Config:
    # pylint: disable=too-few-public-methods
    """Set app configuration from environment variables."""

    ENVIRONMENT = environ.get('ENVIRONMENT')

    FLASK_APP = 'wsgi.py'
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = environ.get('SECRET_KEY')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI') or SQLITE_DB
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Static assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    ASSETS_DEBUG = False
    COMPRESSOR_DEBUG = False
