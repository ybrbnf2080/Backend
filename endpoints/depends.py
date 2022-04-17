from re import U
from sqlalchemy.orm import scoped_session
from fastapi import Depends, HTTPException, status
from db.repositories.users import UserRepository
from db.repositories.jobs import JobRepository
from db.base import Session #as database ### ! CHANGE
from core.security import JWTBearer, decode_access_token
from models.user import User


def get_user_repository() -> UserRepository:
    userRepository = UserRepository(Session())
    try:
        yield userRepository
    finally:
        userRepository.database.close()


def get_job_repository() -> JobRepository:
    jobRepository = JobRepository(Session())
    try:
        yield jobRepository
    finally:
        jobRepository.database.close()


async def get_current_user(
        users: UserRepository = Depends(get_user_repository),
        token: str = Depends(JWTBearer()),
) -> User:
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception
    email: str = payload.get("sub")
    if email is None:
        raise cred_exception
    user = await users.get_by_email(email=email)
    if user is None:
        return cred_exception
    return user
