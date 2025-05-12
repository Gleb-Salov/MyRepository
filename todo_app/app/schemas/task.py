from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3)

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False    