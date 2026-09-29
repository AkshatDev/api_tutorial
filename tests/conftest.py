import pytest
from fastapi.testclient import TestClient

from api_tutorial import create_app


@pytest.fixture(scope="module")
def app():
    app = create_app()
    return app


@pytest.fixture(scope="module")
def client(app):

    with TestClient(app) as client:
        yield client
