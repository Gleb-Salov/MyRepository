from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db" 
# Строка подключения к базе данных

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Объект, который управляет подключением к базе данных. 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Сессия для работы с базой данных

Base = declarative_base()

