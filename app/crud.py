# Functions that query the database

from sqlalchemy.orm import Session
from app import models, schemas


def get_bin(db: Session, bin_id: int):
    return db.query(models.Bin).get(bin_id)


def create_bin(db: Session, new_bin: schemas.BinCreate):
    db_bin = models.Bin(**new_bin.dict())
    db.add(db_bin)
    db.commit()
    db.refresh(db_bin)
    return db_bin


def update_bin():
    pass


def remove_bin():
    pass


def get_user(db: Session, user_id: int):
    return db.query(models.User).get(user_id)


def create_user(db: Session, new_user: schemas.UserCreate):
    db_user = models.User(**new_user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user():
    pass


def remove_user():
    pass
