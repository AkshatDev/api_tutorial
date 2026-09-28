from api_tutorial import Database
from sqlalchemy import text
import os


def test_sql_engine():
    """Test if URL is correct and is being parsed properly"""

    db_url = "postgresql+psycopg://user:secret@example:5432/testdb"
    db_obj = Database(db_url)
    assert db_obj.engine.url.database == "testdb"
