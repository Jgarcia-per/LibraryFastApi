from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends, Path
from starlette import status

from models import BookModel
from models.BookModel import Book
from models.BookRequestModel import BookRequest
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
    return db.query(Book).all()

@app.get("/book/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(db: db_dependency, book_id: int = Path(ge=1)):
    """
    Get Book Filter By Book Id
    """
    book_model = db.query(Book).filter(Book.id == book_id).first()
    if book_model is not None:
        return book_model
    raise HTTPException(status_code=404, detail='Not Found')

@app.post("/book/create_book/", status_code=status.HTTP_201_CREATED)
async def create_book(db: db_dependency, book_request: BookRequest):
    """
    Post Create New Book
    """
    book_model = Book(**book_request.dict())

    db.add(book_model)
    db.commit()

@app.put("/book/{book_id}/update", status_code=status.HTTP_204_NO_CONTENT)
async def update_book (db: db_dependency,
                       book_request: BookRequest,
                       book_id: int = Path(ge=1)):
    """
    Put Update Book
    """
    book_model = db.query(Book).filter(Book.id == book_id).first()
    if book_model is None:
        raise HTTPException(status_code=404, detail='Not Found')

    book_model.title       = book_request.title
    book_model.description = book_request.description
    book_model.priority    = book_request.priority
    book_model.complete    = book_request.complete

    db.add(book_model)
    db.commit()

@app.delete("/book/{book_id}/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(db: db_dependency, book_id: int = Path(ge=1)):
    """
    Delete book by id
    """
    book_model = db.query(Book).filter(Book.id == book_id).first()
    if book_model is None:
        raise HTTPException(status_code=404, detail='Not Found')
    db.query(Book).filter(Book.id == book_id).delete()
    db.commit()
