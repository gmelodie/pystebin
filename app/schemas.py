from typing import List
from pydantic import BaseModel

class BinBase(BaseModel):
    name: str = None
    title: str = None


class BinCreate(BinBase):
    owner_id: int
    password: str


class Bin(BinBase):
    id: int
    # TODO: token?

    class Config():
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    # TODO: password?
    # bins: List[Bin] = []

    class Config():
        orm_mode = True
