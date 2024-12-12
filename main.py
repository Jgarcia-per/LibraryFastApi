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

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def read_all(db: db_dependency):
    """
    Get all Book
    """
    return db.query(BookModel.Book).all()

@app.get("/books/{book_id}")
async def read_book(db: db_dependency, book_id: int):
    """
    Get Book Filter By Book Id
    """
    book_model = db.query(BookModel.Book).filter(BookModel.Book.id == book_id).first
    print(book_model)
    if book_model is not None:
        return book_model
