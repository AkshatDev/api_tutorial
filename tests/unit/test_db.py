"""Unit tests for ``Database`` (no real database needed)."""

from api_tutorial import Database


def test_engine_uses_given_url() -> None:
    """The engine is configured from the URL; creating it does not connect."""
    db_url = "postgresql+psycopg://user:secret@example:5432/testdb"
    db_obj = Database(db_url)
    assert db_obj.engine.url.database == "testdb"
