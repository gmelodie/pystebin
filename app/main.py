from fastapi import FastAPI
from app.routers import bins, users

app = FastAPI()


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

