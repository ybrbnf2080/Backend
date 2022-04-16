from databases import Database
from sqlalchemy.orm import sessionmaker, Session

class BaseRepository:
    def __init__(self, database: Session):
        self.database = database