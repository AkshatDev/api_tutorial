import os
from collections.abc import Iterator

import pytest
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from api_tutorial import Base, Database


@pytest.fixture(scope="session")
def engine() -> Iterator[Engine]:
    """Created once per test run: creates the tables, and disposes of the engine at the end."""
    engine = Database(os.environ["DATABASE_URL"]).engine
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()


@pytest.fixture
def session(engine: Engine) -> Iterator[Session]:
    """A new one for every test, rolled back afterwards so tests don't affect each other."""
    with engine.connect() as connection:
        transaction = connection.begin()
        session = Session(bind=connection, join_transaction_mode="create_savepoint")

        yield session

        session.close()
        transaction.rollback()
