from pydantic import BaseModel, EmailStr
from typing import List, Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

class TaskUpdate(TaskBase):
    title: Optional[str] 
    description: Optional[str]

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    tasks: List[TaskRead] = []  

    class Config:
        from_attributes = True

class UserReadWithTasks(BaseModel):
    id: int
    name: str
    email: str
    tasks: List[TaskRead]

    class Config:
        from_attributes = True
