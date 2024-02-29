"""Unit tests for environment config settings"""

from flask import Flask


def test_development_config(flask_app: Flask):
    assert flask_app.config['ENVIRONMENT'] == 'development'
    assert flask_app.config['SECRET_KEY'] != 'Foo?Bar!'
    assert not flask_app.config['TESTING']
    assert flask_app.config['FLASK_DEBUG'] == 'True'
    assert flask_app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite://')


def test_production_config(flask_app: Flask):
    assert flask_app.config['ENVIRONMENT'] == 'production'
    assert flask_app.config['SECRET_KEY'] != 'Foo?Bar!Baz?!'
    assert not flask_app.config['TESTING']
    assert flask_app.config['FLASK_DEBUG'] == 'False'
    assert flask_app.config['SQLALCHEMY_DATABASE_URI'].startswith('mysql+pymysql://')
