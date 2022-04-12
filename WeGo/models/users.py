from pydantic import BaseModel
from datetime import date
from enum import Enum


class UserTypeKind(str, Enum):
    INDIVIDUAL = "individual"
    ENTITY = "entity"


class UserAccountStatusKind(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    TYPING = "typing"


class UserBase(BaseModel):
    userID: str
    userName: str
    email: str
    password: str
    passwordSalt: str
    dateRegistered: date
    userType: UserTypeKind
    accountStatus: UserAccountStatusKind

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    userID: str
    passwordSalt: str
    dateRegistered: date

    class Config:
        orm_mode = True

