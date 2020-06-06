from fastapi import APIRouter
from app.schemas import Bin

router = APIRouter()


@router.get('/')
async def get_bin(name: str):
    return {"name": name}


@router.post('/')
async def create_bin(_bin: Bin):
    return {"name": _bin.name, "title": _bin.title}


@router.put('/')
async def update_bin(_bin: Bin):
    return {"name": _bin.name, "title": _bin.title}


@router.delete('/')
async def delete_bin(_bin: Bin):
    return {"name": _bin.name, "title": _bin.titl}
