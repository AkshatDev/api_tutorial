"""Database fixtures for integration tests (needs the Postgres service from Compose)."""

import os
from collections.abc import Iterator

import pytest
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from api_tutorial import Base, Database


@pytest.fixture(scope="session")
def engine() -> Iterator[Engine]:
    """Create the engine once per test run, create the tables, and dispose of it at the end."""
    engine = Database(os.environ["DATABASE_URL"]).engine
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()


@pytest.fixture
def session(engine: Engine) -> Iterator[Session]:
    """Give each test a new session, rolled back afterwards so tests don't affect each other."""
    with engine.connect() as connection:
        transaction = connection.begin()
        session = Session(bind=connection, join_transaction_mode="create_savepoint")

        yield session

        session.close()
        transaction.rollback()
