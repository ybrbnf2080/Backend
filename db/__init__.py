from .users import User
from .jobs import Job
from .posts import  Post
from .base import Base, engine

def init_db() :
    Base.metadata.create_all(bind=engine)
