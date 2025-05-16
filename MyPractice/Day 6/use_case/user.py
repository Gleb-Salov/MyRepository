from sqlalchemy.orm import Session

from models import User, Task
from schemas import UserCreate, TaskCreate, TaskUpdate

class UserCRUD:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: UserCreate) -> User:
        new_user = User(name=user.name, email=user.email)
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def get_user(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).first()

    def get_all_users(self, skip: int = 0, limit: int = 100):
        return self.session.query(User).offset(skip).limit(limit).all()

    def update_user(self, user_id: int, user: UserCreate):
        self.session_user = self.session.query(User).filter(User.id == user_id).first()
        if self.session_user:
            self.session_user.name = user.name
            self.session_user.email = user.email
            self.session.commit()
            self.session.refresh(self.session_user)
            return self.session_user
        return None

    def delete_user(self, user_id: int):
        self.session_user = self.session.query(User).filter(User.id == user_id).first()
        if self.session_user:
            self.session.delete(self.session_user)
            self.session.commit()
            return self.session_user
        return None

    def get_user_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).first()

    def get_user_with_tasks(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).first()