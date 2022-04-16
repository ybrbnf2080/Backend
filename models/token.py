from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: Int


class Login(BaseModel):
    email: EmailStr
    password: str
