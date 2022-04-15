import datetime
from typing import Optional, List, String, Array
from pydantic import BaseModel, EmailStr, validator, constr
from db.base import Base

class User(BaseModel):
    id : Optional[str] = None
    username: str
    full_name: str
    semail: EmailStr
    hashed_password: str
    profile_photo_url: str
    profile_photo_url_hd: str
    biography: str
    external_url: str
    business_category: List[str]
    age_approx: str
    age_group: str
    gender: str
    langs: List[str]
    is_private: bool
    is_verified: bool
    is_business_account: bool
    is_company: bool
    followers_count: int
    followings_count: int
    posts_count: int
    highlight_reels_count: int
    latest_location_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)
    password2: str
    is_company: bool = False

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values["password"]:
            raise ValueError("passwords don't match")
        return v

