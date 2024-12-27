from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from env import USER_DB, PASSWORD_DB, HOST_DB, NAME_DB

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}/{NAME_DB}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    Start DataBase
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
