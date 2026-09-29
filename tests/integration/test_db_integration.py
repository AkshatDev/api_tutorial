import os

from sqlalchemy import text

from api_tutorial import Database


def test_sql_connection():
    """Test if connection with the DB can be done."""

    db_url = os.environ["DATABASE_URL"]
    db_obj = Database(db_url)
    with db_obj.engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        value = result.scalar_one()
        assert value == 1
