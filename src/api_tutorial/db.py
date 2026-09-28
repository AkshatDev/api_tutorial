from sqlalchemy import Engine, create_engine

class Database:
    def __init__(self, url :str)-> None:
        """ Initialize the class with a DB URL."""
        self.engine: Engine = create_engine(url)