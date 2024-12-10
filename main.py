"""
Main module of a library

"""
from fastapi import FastAPI
from Models.BookModel import Book, BookRequest
from Services.BookService import find_book_id
from Configs.Data import BOOKS

app = FastAPI()

# -------- GET -------------
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
        if book.book_id == book_id:
            return book

@app.get("/books/rating/")
async def read_book_by_rating(book_rating: int):
    """
    Read books by rating
    """
    books_to_return= []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.get("/books/published_date/")
async def read_book_by_published_date(publishade_date: int):
    """
    Read books by published date
    """
    books_to_return=[]
    for book in BOOKS:
        if book.published_date == publishade_date:
            books_to_return.append(book)
    return books_to_return

# -------- POST -------------

@app.post("/books/new_book")
async def create_book(book_request: BookRequest):
    """
    Create new books
    """
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

# -------- PUT -------------

@app.put("/books/update_book")
async def update_book(book: BookRequest):
    """
    Update Book
    """
    for i in range(len(BOOKS)): # [consider-using-enumerate] / C0200
        if BOOKS[i].book_id == book.book_id:
            BOOKS[i] = book

# -------- DELETE -------------

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)): # [consider-using-enumerate] / C0200
        if BOOKS[i].book_id == book_id:
            BOOKS.pop(i)
            break
