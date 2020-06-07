from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    # TODO: hash password
    password = Column(String)

    bins = relationship("Bin", back_populates="owner")


class Bin(Base):
    __tablename__ = "bins"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, index=True)
    title = Column(String)
    text = Column(String)
    password = Column(String)
    # TODO: token

    owner = relationship("User", back_populates="bins")
