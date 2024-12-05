# LibraryFastApi

This project is a simple FastAPI application that manages a collection of books. It provides endpoints to create, read, update, and delete books from the collection.

## Requirements

It is recommended to use a virtual environment to manage dependencies. To create and activate a virtual environment, run the following commands:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Linux/macOS)
source venv/bin/activate

# Activate the virtual environment (Windows)
.\venv\Scripts\activate
```

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Project Structure

- **books.py**: Contains the FastAPI application with various endpoints to manage books.
- **requirements.txt**: Lists all the dependencies required for the project.

## Endpoints

### Get All Books

- **URL**: `/books`
- **Method**: `GET`
- **Description**: Retrieves all books in the collection.

### Get Book by Title

- **URL**: `/books/title/{book_title}`
- **Method**: `GET`
- **Description**: Retrieves a book by its title.

### Get Books by Author

- **URL**: `/books/author/{books_author}`
- **Method**: `GET`
- **Description**: Retrieves books by a specific author.

### Get Books by Category

- **URL**: `/books/category/`
- **Method**: `GET`
- **Description**: Retrieves books by a specific category. Requires a query parameter `category`.

### Get Books by Author and Category

- **URL**: `/books/{book_author}/`
- **Method**: `GET`
- **Description**: Retrieves books by a specific author and category. Requires a query parameter `category`.

### Create a New Book

- **URL**: `/books/create_book/`
- **Method**: `POST`
- **Description**: Creates a new book entry. Requires a JSON body with book details.

### Update a Book

- **URL**: `/books/update_book/`
- **Method**: `PUT`
- **Description**: Updates an existing book. Requires a JSON body with updated book details.

### Delete a Book

- **URL**: `/books/delete_book/{book_title}`
- **Method**: `DELETE`
- **Description**: Deletes a book by its title.

## Running the Application

To run the FastAPI application, execute:

```bash
uvicorn books:app --reload
```

This will start the server on `http://127.0.0.1:8000`.

## License

This project is licensed under the MIT License.