from Configs.Data import BOOKS
from Models.BookModel import Book

def find_book_id(book: Book) -> Book:
    """
    Automatically increment id field
    """
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    
    return book