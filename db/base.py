#from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import DATABASE_URL

#database = Database(DATABASE_URL)
#metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
    future=True,
)


Session = sessionmaker(autocommit=False, autoflush=False, bind=engine,future=True )

Base = declarative_base()

#Base.query = db_session.query_property()

