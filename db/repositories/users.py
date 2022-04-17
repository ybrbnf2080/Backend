import datetime
from typing import List, Optional
from unittest import result
from db.models.users import User as Users
from models.user import User, UserIn
from core.security import hash_password
from .base import BaseRepository
from sqlalchemy import insert, select, update



class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = select(Users).limit(limit).offset(skip)
        result = self.database.execute(query).scalars().all()
        users = map(UserRepository.serilaese, result)
        clearUsers = map(UserRepository.delete_password, users)
        return list(clearUsers)

    async def get_by_id(self, id: int) -> Optional[User]:
        query = select(Users).where(Users.id == id)
        result = self.database.execute(query).scalars().one_or_none()

        if user is None:
            return None
        user = UserRepository.serilaese(result)
        clearUser = UserRepository.delete_password(user)
        return clearUser
    
    async def get_by_email(self, email: str) -> User:
        query = select(Users).filter(Users.email == email)
        result = self.database.execute(query).scalars().one_or_none() 

        if result is None:
            return None
        return UserRepository.serilaese(result)
    
    async def create(self, u: UserIn) -> User:
        if (u.username is None) : u.username = (u.full_name + hash_password(u.email)[-2:].upper() )
        user = User(
            username=u.username  ,
            full_name=u.full_name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop("id", None)
        query = insert(Users).values(**values).returning(Users)
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
        query = update(Users).where(Users.id == id).values(**values).returning(Users)
        result = self.database.execute(query).one()
        self.database.commit() 
        
        return User.parse_obj(result._mapping)

    @staticmethod
    def serilaese(userRow: any):
        return User.parse_obj(userRow.__dict__)
    
    @staticmethod
    def delete_password(user: User) :
        user.hashed_password = None
        return user
