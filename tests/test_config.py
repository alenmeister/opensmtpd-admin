"""Unit tests for environment config settings"""


def test_development_config(flask_app):
    assert flask_app.config['SECRET_KEY'] != 'Foo?Bar!'


def test_production_config(flask_app):
    assert flask_app.config['SECRET_KEY'] != 'Foo?Bar!Baz?!'
