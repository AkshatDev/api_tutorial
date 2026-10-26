"""Integration test: the app can reach the real Postgres database."""

import os

from sqlalchemy import text

from api_tutorial import Database


def test_sql_connection() -> None:
    """Connect using ``DATABASE_URL`` and run a trivial query."""
    db_url = os.environ["DATABASE_URL"]
    db_obj = Database(db_url)
    with db_obj.engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        value = result.scalar_one()
        assert value == 1
