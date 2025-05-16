from fastapi import FastAPI

from database import Base, engine
from routers import users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)