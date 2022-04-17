from .models.users import User
from .models.jobs import Job
from .models.posts import  Post
from db.base import Base, engine

def init_db() : # RUDIMENT
    Base.metadata.create_all(bind=engine)
