from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped
from MyPractice.day6.service_layer.sqlalchemy.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    tasks = relationship("Task",back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User id={self.id} name={self.name!r} email={self.email!r}>"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index =True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")

    def __repr__(self):
        return f"<Task id={self.id} title={self.title!r} user_id={self.user_id}>"
