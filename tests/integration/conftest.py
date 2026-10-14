import os

import pytest
from sqlalchemy import Engine
from sqlalchemy.orm import Session

import api_tutorial.models  # noqa: F401, for setting up DB model class
from api_tutorial import Base, Database


@pytest.fixture(scope="session")
def engine():
    engine = Database(os.environ["DATABASE_URL"]).engine
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()


@pytest.fixture
def session(engine: Engine):
    with engine.connect() as connection:
        transaction = connection.begin()
        session = Session(bind=connection, join_transaction_mode="create_savepoint")

        yield session

        session.close()
        transaction.rollback()
