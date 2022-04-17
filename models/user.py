import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, validator, constr
from db.base import Base

class User(BaseModel):
    id : Optional[int] = None
    username: str
    full_name: Optional[str]
    email: EmailStr
    hashed_password: Optional[str]
    profile_photo_url: Optional[str] 
    profile_photo_url_hd: Optional[str] 
    biography: Optional[str] 
    external_url: Optional[str] 
    business_category: Optional[List[str]]
    age_approx: Optional[str] 
    age_group: Optional[str] 
    gender: Optional[str] 
    langs: Optional[List[str]]
    is_private: Optional[bool] 
    is_verified: Optional[bool] 
    is_business_account: Optional[bool] 
    is_company: Optional[bool] 
    followers_count: Optional[int] 
    followings_count: Optional[int] 
    posts_count: Optional[int] 
    highlight_reels_count: Optional[int] 
    latest_location_id: Optional[str] 
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True


class UserIn(BaseModel):
    username: str | None =None
    full_name: str
    email: EmailStr
    password: constr(min_length=8)
    is_company: bool = False
