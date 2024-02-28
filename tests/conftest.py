"""Global pytest fixtures"""
import pytest

from src import create_app


@pytest.fixture(scope='function')
def flask_app():
    app = create_app()
    return app
