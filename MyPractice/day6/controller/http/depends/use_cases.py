from sqlalchemy.orm import Session
from fastapi import Depends

from MyPractice.day6.service_layer.sqlalchemy.session import get_db
from MyPractice.day6 import use_case

def get_user_crud(
  session: Session = Depends(get_db),
) -> use_case.UserCRUD:
  return use_case.UserCRUD(session=session)

def get_task_crud(
  session: Session = Depends(get_db),
) -> use_case.TaskCRUD:
  return use_case.TaskCRUD(session=session)