import pytest

from api_tutorial import create_app


@pytest.fixture
def app():

    app = create_app()
    app.testing = True
    return app


@pytest.fixture
def client(app):

    client = app.test_client()
    return client
