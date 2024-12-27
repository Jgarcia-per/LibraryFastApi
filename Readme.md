# LibraryFastApi

LibraryFastApi is a project designed to manage a library system using FastAPI. It includes functionalities for managing books and users, with features such as user authentication, book creation, updating, and deletion.

## Features

- **User Management**: Create, read, update, and delete users.
- **Book Management**: Create, read, update, and delete books.
- **Authentication**: Secure user authentication using JWT tokens.
- **Database Integration**: Uses PostgreSQL for data storage.
- **Testing**: Comprehensive unit tests for services and routes.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/LibraryFastApi.git
    cd LibraryFastApi
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:

    ```sh
    cp .env.example .env
    # Edit the .env file with your database and secret key configurations
    ```

5. Run the database migrations:

    ```sh
    alembic upgrade head
    ```

6. Start the FastAPI server:

    ```sh
    uvicorn main:app --reload
    ```

## Usage

- Access the API documentation at `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`.
- Use the provided endpoints to manage users and books.

## Running Tests

To run the tests, use the following command:

```sh
pytest
```
