import pytest
from fastapi.testclient import TestClient

from fastapi import FastAPI

from app.routers import bins, users
from app.database import engine
from app import models, schemas, crud, utils

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    bins.router,
    prefix='/bins',
    tags=["bins"],
)
app.include_router(
    users.router,
    prefix='/users',
    tags=["users"],
)


client = TestClient(app)

USERNAME_USER1 = "user1"
PASSWORD_USER1 = "pass1"


def test_create_user():
    params = {"username":USERNAME_USER1, "password":PASSWORD_USER1}
    response = client.post("/users/", json=params)
    assert response.status_code == 200


def test_create_user_without_password():
    params = {"username":USERNAME_USER1}
    response = client.post("/users/", json=params)
    assert response.status_code == 422


def test_get_user():
    params = {"username":USERNAME_USER1}
    response = client.get("/users/", params=params)
    assert response.status_code == 200
    assert response.json() == {
        "username": USERNAME_USER1,
        "password": PASSWORD_USER1,
    }


def test_get_inexistent_user():
    params = {"username":"notregistered"}
    response = client.get("/users/", params=params)
    assert response.status_code == 404
