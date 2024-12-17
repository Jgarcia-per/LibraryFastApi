# LibraryFastApi

Este proyecto es una API RESTful construida con FastAPI para gestionar una biblioteca. Permite la creación, lectura, actualización y eliminación de libros y usuarios.

## Requisitos

- Python 3.8+
- FastAPI
- SQLAlchemy
- SQLite

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/LibraryFastApi.git
    cd LibraryFastApi
    ```

2. Crea un entorno virtual e instala las dependencias:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## Uso

1. Inicia el servidor:

    ```bash
    uvicorn main:app --reload
    ```

2. Accede a la documentación interactiva de la API en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Endpoints

### Autenticación

- `POST /v1/auth/create`: Crear un nuevo usuario.
- `POST /v1/auth/token`: Autenticar un usuario y obtener un token.

### Libros

- `GET /v1/book/`: Obtener todos los libros.
- `GET /v1/book/{book_id}`: Obtener un libro por su ID.
- `POST /v1/book/create_book/`: Crear un nuevo libro.
- `PUT /v1/book/{book_id}/update`: Actualizar un libro existente.
- `DELETE /v1/book/{book_id}/delete`: Eliminar un libro por su ID.

## Modelos

### Usuario

- `username`: str
- `email`: str
- `first_name`: str
- `last_name`: str
- `password`: str
- `role`: str

### Libro

- `title`: str
- `description`: str
- `priority`: int
- `complete`: bool
