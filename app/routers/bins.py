from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import Bin, BinCreate
from app.utils import get_db
from app import crud

router = APIRouter()


@router.get('/')
async def get_bin(_bin: Bin, db: Session = Depends(get_db)):
    # TODO: test if user does not exist
    return crud.get_bin(db, _bin.id)


@router.post('/')
async def create_bin(_bin: BinCreate, db: Session = Depends(get_db)):
    # TODO: test if user already exists
    return crud.create_bin(db, _bin)


@router.put('/')
async def update_bin(_bin: Bin):
    return {"name": _bin.name, "title": _bin.title}


@router.delete('/')
async def delete_bin(_bin: Bin):
    return {"name": _bin.name, "title": _bin.titl}
