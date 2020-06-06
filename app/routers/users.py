from fastapi import APIRouter
from app.schemas import User

router = APIRouter()


@router.get('/')
async def get_user(username: str):
    return {"username": username}


@router.post('/')
async def create_user(new_user: User):
    return {"username": new_user.username}


@router.put('/')
async def update_user(user: User):
    return {"username": user.username}


@router.delete('/')
async def delete_user(user: User):
    return {"username": user.username}
