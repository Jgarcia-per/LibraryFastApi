from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from typing import Annotated

from models.BookModel import Book
from models.BookRequestModel import BookRequest
from configs.Database import db_dependency
from services.UserService import get_current_user

BookRouter = APIRouter()
user_dependency = Annotated[dict, Depends(get_current_user)]


@BookRouter.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    """
    Get all Books
    """
    return db.query(Book).all()

@BookRouter.get("/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(db: db_dependency, book_id: int = Path(ge=1)):
    """
    Get Book Filter By Book Id
    """
    book_model = db.query(Book).filter(Book.id == book_id).first()
    if book_model is not None:
        return book_model
    raise HTTPException(status_code=404, detail='Not Found')

@BookRouter.post("/create_book/", status_code=status.HTTP_201_CREATED)
async def create_book(user: user_dependency, db: db_dependency, book_request: BookRequest):
    """
    Post Create New Book
    """
    if user is None:
        raise HTTPException(status_code=401, detail="unauthorized")
    book_model = Book(**book_request.dict())

    db.add(book_model)
    db.commit()

@BookRouter.put("/{book_id}/update", status_code=status.HTTP_204_NO_CONTENT)
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

@BookRouter.delete("/{book_id}/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(db: db_dependency, book_id: int = Path(ge=1)):
    """
    Delete book by id
    """
    book_model = db.query(Book).filter(Book.id == book_id).first()
    if book_model is None:
        raise HTTPException(status_code=404, detail='Not Found')
    db.query(Book).filter(Book.id == book_id).delete()
    db.commit()
