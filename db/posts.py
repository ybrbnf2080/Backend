from sqlalchemy import ARRAY, Column, ForeignKey, Integer, DateTime, Boolean, String 
from sqlalchemy.orm import relationship
from .base import Base
import datetime

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column( Integer, ForeignKey('users.id'), nullable=False)
    shortcode = Column(String, unique=True)
    created_time = Column(DateTime, default=datetime.datetime.utcnow)
    timestamp = Column(Integer)
    product_type = Column(String)
    text = Column(String)
    text_lang = Column(String)
    text_tagged_users = Column(ARRAY(Integer))
    text_tags = Column(ARRAY(String))
    attached_media_display_url = Column(String)
    attached_media_content = Column(ARRAY(String))
    attached_media_tagged_users = Column(ARRAY(String))
    is_video = Column(Boolean)
    is_comments_disabled = Column(Boolean)
    like_count = Column(Integer)
    comments_count = Column(Integer)
    video_views_count = Column(Integer)
    video_plays_count = Column(Integer)
    related_posts = Column(ARRAY(String))
    sponsors = Column(ARRAY(Integer))
    owner_id = Column(Integer, unique=True)
    location_id = Column(Integer, unique=True)

    user = relationship("User", back_populates="posts")
    