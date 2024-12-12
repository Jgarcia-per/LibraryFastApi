from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from models import BookModel
from configs.Database import engine, SessionLocal

app = FastAPI()
BookModel.Base.metadata.create_all(bind=engine)

def get_db():
    """
    Start DataBase
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)]):
    """
    Get all Book
    """
    return db.query(BookModel.Book).all()
