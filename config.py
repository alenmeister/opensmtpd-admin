"""Application config"""

from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Set app configuration from environment variables."""

    ENVIRONMENT = environ.get('ENVIRONMENT')

    FLASK_APP = 'app.py'
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = environ.get('SECRET_KEY')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
