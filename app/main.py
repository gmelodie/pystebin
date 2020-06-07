from fastapi import FastAPI
from app.routers import bins, users
from app import models, schemas, crud
from app.database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get('/')
async def root():
    return {"message": "Hello World"}


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

