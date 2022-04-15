from sqlalchemy import ARRAY, Column, Integer, DateTime, Boolean, String 
from sqlalchemy.orm import relationship
from .base import Base
import datetime

class User(Base):
    __tablename__ = "users"
    
    id  =  Column(Integer, primary_key=True, autoincrement=True)
    username =  Column(String, nullable=False, unique=True)
    full_name =  Column(String,)
    email = Column(String, nullable=False, unique=True)
    hashed_password =  Column(String, nullable=False)
    profile_photo_url = Column(String, )
    profile_photo_url_hd = Column(String)
    biography = Column(String)
    external_url = Column(String, unique=True)
    business_category = Column(ARRAY(String), )
    age_approx = Column(Integer, )
    age_group = Column(String, )
    gender = Column(String)
    langs = Column(ARRAY(String), )
    is_private = Column(Boolean)
    is_verified = Column(Boolean)
    is_business_account = Column(Boolean)
    is_company = Column(Boolean)
    followers_count = Column(Integer, )
    followings_count = Column(Integer, )
    posts_count = Column(Integer, )
    highlight_reels_count = Column(Integer, )
    latest_location_id = Column(Integer, )
    created_at =  Column(DateTime, default=datetime.datetime.utcnow)
    updated_at =  Column(DateTime, default=datetime.datetime.utcnow)

    jobs= relationship("Job", back_populates="user")
    posts= relationship("Post", back_populates="user")
