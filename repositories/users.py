import datetime
from typing import List, Optional
from unittest import result
from db.users import User as users
from models.user import User, UserIn
from core.security import hash_password
from .base import BaseRepository
from sqlalchemy import insert, select, update

class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = select(users).limit(limit).offset(skip)
        result = self.database.execute(query).scalars().all()
        return result

    async def get_by_id(self, id: int) -> Optional[User]:
        query = select(users).where(users.id == id)
        user = self.database.execute(query).scalars().one()
        if user is None:
            return None
        return User.parse_obj(user.__dict__)

    async def create(self, u: UserIn) -> User:
        user = User(
            username=u.username,
            full_name=u.full_name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop("id", None)
        query = insert(users).values(**values).returning(users)
        result = self.database.execute(query).one() # returned obj ? :/ ?
        self.database.commit()
        return User.parse_obj(result._mapping)

    async def update(self, id: int, u: UserIn) -> User:
        user = User(
            id=id,
            username=u.username,
            full_name= u.full_name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(), 
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop("created_at", None)
        values.pop("id", None)
        query = update(users).where(users.id == id).values(**values).returning(users)
        result = self.database.execute(query).one()
        self.database.commit() 
        
        return User.parse_obj(result._mapping)

    async def get_by_email(self, email: str) -> User:
        query = select(users).filter(users.email == email)
        print(query)
        user = self.database.execute(query)
        user_obj = user.scalars().one_or_none() # returned ROW obj
           
        if user is None:
            return None
        return User.parse_obj(user_obj.__dict__)
