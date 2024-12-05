from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Two', 'category': 'math'},
    ]

@app.get("/books")
async def read_all_books():
    """
    Asynchronously retrieves all books.

    Returns:
        list: A list of all books.
    """
    return BOOKS

@app.get("/books/title/{book_title}")
async def read_book_tittle(book_tittle: str):
    """
    Retrieve a book from the BOOKS collection by its title.

    Args:
        book_tittle (str): The title of the book to search for.

    Returns:
        dict: The book details if found, otherwise an error message.
    """
    for book in BOOKS:
        if book.get('title').casefold() == book_tittle.casefold():
            return book
    return {'error': 'Book not found'}

@app.get("/books/author/{books_author}")
async def read_book_author(books_author: str):
    """
    Retrieve a list of books by a specific author.

    Args:
        books_author (str): The name of the author to search for.

    Returns:
        list: A list of dictionaries, each representing a book by the specified author.
    """
    result_books = []
    for book in BOOKS:
        if book.get('author').casefold() == books_author.casefold():
            result_books.append(book)
    return result_books


@app.get("/books/category/")
async def read_category_by_query(category: str):
    """
    Asynchronously reads and returns books that match the given category.
    Args:
        category (str): The category to filter books by.
    Returns:
        list: A list of books that belong to the specified category.
    """

    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    """
    Asynchronously retrieves books by author and category.
    This function searches through a predefined list of books (BOOKS) and returns a list of books
    that match the specified author and category. The search is case-insensitive.
    Args:
        book_author (str): The author of the book to search for.
        category (str): The category of the book to search for.
    Returns:
        list: A list of books that match the specified author and category.
    """

    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() \
            and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book/")
async def create_book(new_book: dict = Body()):
    """
    Asynchronously creates a new book entry.
    Args:
        new_book (dict): A dictionary containing the details of the new book.
    Returns:
        None
    """

    BOOKS.append(new_book)

@app.put("/books/update_book/")
async def update_book(update_book: dict = Body()):
    """
    Update a book in the BOOKS list.
    This asynchronous function takes a dictionary representing the updated book details
    and searches for a book with the same title in the BOOKS list. If a match is found,
    the book is updated with the new details.
    Args:
        update_book (dict): A dictionary containing the updated book details. The dictionary
                            must include a 'title' key to identify the book to be updated.
    Returns:
        dict: A dictionary containing a message indicating that the book was updated.
    """

    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold(): 
            BOOKS[i] = update_book
            return {'message': 'Book updated'}

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    """
    Delete a book from the BOOKS list by its title.

    Args:
        book_title (str): The title of the book to be deleted.

    Returns:
        None
    """

    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
