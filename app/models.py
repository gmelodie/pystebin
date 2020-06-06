from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    # hashed_password = Column(String)

    bins = relationship("Bin", backpopulates="owner")


class Bin(Base):
    __tablename__ = "bins"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, index=True)
    text = Column(String)
    # TODO: token
    # TODO: password

    owner = relationship("User", backpopulates="bins")
