from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends, Path
from starlette import status

from models import BookModel, BookRequestModel
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

@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    """
    Get all Book
    """
    return db.query(BookModel.Book).all()

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(db: db_dependency, book_id: int = Path(ge=1)):
    """
    Get Book Filter By Book Id
    """
    book_model = db.query(BookModel.Book).filter(BookModel.Book.id == book_id).first()
    if book_model is not None:
        return book_model
    raise HTTPException(status_code=404, detail='Not Found')

@app.post("/book/create_book/", status_code=status.HTTP_201_CREATED)
async def create_book(db: db_dependency, book_request: BookRequestModel.BookRequest):
    """
    Post Create New Book
    """
    book_model = BookModel.Book(**book_request.dict())

    db.add(book_model)
    db.commit()
