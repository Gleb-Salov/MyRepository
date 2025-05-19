from sqlalchemy.orm import Session

from MyPractice.day6.repository.sqlite.models import Task
from MyPractice.day6.controller.http.schemas.schemas import TaskCreate, TaskUpdate

class TaskCRUD:
    def __init__(self, session: Session):
        self.session = session

    def create_task(self, task: TaskCreate, user_id: int):
        session_task = Task(**task.dict(), user_id=user_id) 
        self.session.add(session_task)  
        self.session.commit()  
        self.session.refresh(session_task)  
        return session_task 

    def get_task(self, task_id: int):
        return self.session.query(Task).filter(Task.id == task_id).first()

    def get_user_tasks(self, user_id: int, skip: int = 0, limit: int = 100):
        return self.session.query(Task).filter(Task.user_id == user_id).offset(skip).limit(limit).all()

    def update_task(self, task_id: int, task: TaskUpdate):
        self.session_task = self.session.query(Task).filter(Task.id == task_id).first()
        if self.session_task:
            for var, value in vars(task).items():
                setattr(self.session_task, var, value) if value else None
            self.session.commit()
            self.session.refresh(self.session_task)
            return self.session_task
        return None

    def delete_task(self, task_id: int) -> None:
        self.session_task = self.session.query(Task).filter(Task.id == task_id).first() 
        if self.session_task:
            self.session.delete(self.session_task)
            self.session.commit()
            return self.session_task
        return None       