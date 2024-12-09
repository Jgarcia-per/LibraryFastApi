"""
Main module of a library

"""
from fastapi import FastAPI
from Models.BookModel import Book, BookRequest
from Services.BookService import find_book_id
from Configs.Data import BOOKS

app = FastAPI()

@app.get("/books")
async def read_allbooks():
    """
    Call all books
    """
    return BOOKS

@app.get("/books/{book_id}")
async def read_books(book_id: int):
    """
    Read books by author
    """
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.get("/books/rating/")
async def ready_book_by_rating(book_rating: int):
    """
    Read books by rating
    """
    books_to_return= []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.post("/books/new_book")
async def create_book(book_request: BookRequest):
    """
    Create new books
    """
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
