from pydantic import BaseModel


class User(BaseModel):
    username: str
    # TODO: list of bins
    # password: str = None


class Bin(BaseModel):
    name: str
    title: str
    # TODO: password
    # TODO: token?

