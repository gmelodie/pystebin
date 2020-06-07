from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import User, UserCreate
from app.utils import get_db
from app import crud

router = APIRouter()


@router.get('/')
async def get_user(user: User, db: Session = Depends(get_db)):
    #TODO: test if user does not exist
    return crud.get_user(db, user.id)


@router.post('/')
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    #TODO: test if user exists
    return crud.create_user(db, user)


@router.put('/')
async def update_user(user: User):
    return {"username": user.username}


@router.delete('/')
async def delete_user(user: User):
    return {"username": user.username}
