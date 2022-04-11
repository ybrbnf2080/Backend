from typing import List

from fastapi import Depends

from sqlalchemy.orm import Session

from WeGo.database.sessions import get_session
from WeGo.database.tables.users import User

from WeGo.models.users import UserCreate


class UsersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_users_list(self) -> List[User]:
        users = (
            self.session
            .query(User)
            .all()
        )
        return users

    def create_user(self, user_data: UserCreate) -> User:
        user = User(**user_data.dict())
        self.session.add(user)
        self.session.commit()
        return user

