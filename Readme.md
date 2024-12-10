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

- **main.py**: Contains the main FastAPI application with various endpoints to manage books.
- **Models/BookModel.py**: Defines the `Book` and `BookRequest` models.
- **Services/BookService.py**: Contains the service logic for book operations.
- **Configs/Data.py**: Contains the initial data for the books collection.
- **requirements.txt**: Lists all the dependencies required for the project.

## Endpoints

### Main Application Endpoints (main.py)

#### Get All Books

- **URL**: `/books`
- **Method**: `GET`
- **Description**: Retrieves all books in the collection.

#### Get Book by ID

- **URL**: `/books/{book_id}`
- **Method**: `GET`
- **Description**: Retrieves a book by its ID.

#### Get Books by Rating

- **URL**: `/books/rating/`
- **Method**: `GET`
- **Description**: Retrieves books by a specific rating. Requires a query parameter `book_rating`.

#### Get Books by Published Date

- **URL**: `/books/published_date/`
- **Method**: `GET`
- **Description**: Retrieves books by a specific published date. Requires a query parameter `publishade_date`.

#### Create a New Book

- **URL**: `/books/new_book`
- **Method**: `POST`
- **Description**: Creates a new book entry. Requires a JSON body with book details.

#### Update a Book

- **URL**: `/books/update_book`
- **Method**: `PUT`
- **Description**: Updates an existing book entry. Requires a JSON body with updated book details.

#### Delete a Book

- **URL**: `/books/{book_id}`
- **Method**: `DELETE`
- **Description**: Deletes a book by its ID.

## Running the Application

To run the main FastAPI application, execute:

```bash
uvicorn main:app --reload
```

This will start the server on `http://127.0.0.1:8000`.
