from fastapi import APIRouter
from fastapi import Depends

from WeGo.models.users import UserCreate, UserBase

from typing import List

from WeGo.services.users.users import UsersService

router = APIRouter(
    prefix="/users"
)


@router.get("/", response_model=List[UserBase])
async def get_users_list(service: UsersService = Depends()):
    return service.get_users_list()


@router.post("/", response_model=UserBase)
async def create_user(
        user_data: UserBase,
        service: UsersService = Depends(),
):
    return service.create_user(user_data)
