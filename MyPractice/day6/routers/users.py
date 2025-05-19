from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User  
from database import SessionLocal
from schemas import UserCreate, UserRead
from typing import List
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

@router.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    existing_user = crud.get_user(db, user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return existing_user

@router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    user = crud.update_user(db, user_id, user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    existing_user = crud.delete_user(db, user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return None

@router.get("/users/", response_model=List[UserRead])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_users(db, skip=skip, limit=limit)

