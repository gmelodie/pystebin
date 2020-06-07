from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.schemas import User, UserCreate
from app.utils import get_db
from app import crud

router = APIRouter()


@router.get('/', status_code=200)
async def get_user(username: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username)

    if not user: #TODO: enhance
        error =  {"error": "no such user"}
        return JSONResponse(status_code=404, content=error)

    return {"username": user.username, "password": user.password}


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
