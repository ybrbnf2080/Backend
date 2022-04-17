from sqlalchemy import ARRAY, Column, Integer, DateTime, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base
import datetime

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column( Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column( Integer, ForeignKey('users.id'), nullable=False)
    title = Column( String)
    description = Column( String)
    salary_from = Column( Integer)
    salary_to = Column( Integer)
    is_active = Column( Boolean)
    created_at = Column( DateTime, default=datetime.datetime.utcnow)
    updated_at = Column( DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="jobs")