from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    bins: List[Bin] = []

    class Config():
        orm_mode = True


class BinBase(BaseModel):
    name: str
    title: str = None


class BinCreate(BinBase):
    owner_id: int
    password: str


class Bin(BinBase):
    id: int
    content: str
    # TODO: token?

    class Config():
        orm_mode = True
