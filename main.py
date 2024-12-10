"""
Main module of a library

"""
from fastapi import FastAPI, HTTPException, Path, Query
from Models.BookModel import Book, BookRequest
from starlette import status
from Services.BookService import find_book_id
from Configs.Data import BOOKS

app = FastAPI()

# -------- GET -------------
@app.get("/books", status_code=status.HTTP_200_OK)
async def read_allbooks():
    """
    Call all books
    """
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_books(book_id: int = Path(ge=1)):
    """
    Read books by author
    """
    for book in BOOKS:
        if book.book_id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')

@app.get("/books/rating/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(ge=0)):
    """
    Read books by rating
    """
    books_to_return= []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.get("/books/published_date/", status_code=status.HTTP_200_OK)
async def read_book_by_published_date(publishade_date: int = Query(ge=-3000)):
    """
    Read books by published date
    """
    books_to_return=[]
    for book in BOOKS:
        if book.published_date == publishade_date:
            books_to_return.append(book)
    return books_to_return

# -------- POST -------------

@app.post("/books/new_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    """
    Create new books
    """
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

# -------- PUT -------------

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    """
    Update Book
    """
    book_changed = False
    for i in range(len(BOOKS)): # [consider-using-enumerate] / C0200
        if BOOKS[i].book_id == book.book_id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

# -------- DELETE -------------

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(ge=0)):
    """
    Delete Book
    """
    book_changed = False
    for i in range(len(BOOKS)): # [consider-using-enumerate] / C0200
        if BOOKS[i].book_id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')
