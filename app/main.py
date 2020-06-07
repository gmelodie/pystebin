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


@app.get('/')
async def root():
    return {"message": "Hello World"}


