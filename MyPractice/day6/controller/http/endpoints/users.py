from typing import List
from MyPractice.day6 import use_case

from fastapi import APIRouter, Depends, HTTPException

from MyPractice.day6.controller.http.depends.use_cases import get_user_crud, get_task_crud
from MyPractice.day6.controller.http.schemas.schemas import UserCreate, UserRead, UserReadWithTasks, TaskCreate, TaskRead

router = APIRouter()

@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate, user_crud: use_case.UserCRUD = Depends(get_user_crud)):
    existing_user = user_crud.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(user)

@router.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int, user_crud: use_case.UserCRUD = Depends(get_user_crud)):
    existing_user = user_crud.get_user(user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return existing_user

@router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_crud: use_case.UserCRUD = Depends(get_user_crud)):
    user = user_crud.update_user(user_id, user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, user_crud: use_case.UserCRUD = Depends(get_user_crud)):
    existing_user = user_crud.delete_user(user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return None

@router.get("/users/", response_model=List[UserRead])
def get_users(skip: int = 0, limit: int = 100, user_crud: use_case.UserCRUD = Depends(get_user_crud)):
    return user_crud.get_all_users(skip=skip, limit=limit)

@router.get("/users/{user_id}/tasks", response_model=UserReadWithTasks)
def get_user_with_tasks(user_id: int, user_crud: use_case.UserCRUD = Depends(get_user_crud)):
    user = user_crud.get_user_with_tasks(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/{user_id}/tasks", response_model=TaskRead)
def create_task(user_id: int, task: TaskCreate, task_crud: use_case.TaskCRUD = Depends(get_task_crud)):
    db_task = task_crud.create_task(task, user_id)
    return db_task

@router.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(task_id: int, task_crud: use_case.TaskCRUD = Depends(get_task_crud)):
    db_task = task_crud.get_task(task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
    
@router.get("/users/{user_id}/tasks/", response_model=List[TaskRead])
def get_task(user_id: int, skip: int = 0, limit: int = 100, task_crud: use_case.TaskCRUD = Depends(get_task_crud)):
    return task_crud.get_user_tasks(user_id, skip, limit)