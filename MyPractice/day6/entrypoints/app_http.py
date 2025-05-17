from fastapi import FastAPI

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from MyPractice.day6.service_layer.sqlalchemy.database import Base, engine
from MyPractice.day6.controller.http.endpoints import users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)