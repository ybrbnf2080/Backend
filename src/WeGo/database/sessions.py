from sqlalchemy.orm import sessionmaker
from .connection import engine

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
