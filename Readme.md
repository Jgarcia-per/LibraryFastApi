# LibraryFastApi

Este proyecto es una API para la gestión de una biblioteca, desarrollada con FastAPI. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre libros y usuarios.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado:

- Python 3.8 o superior
- PostgreSQL

## Instalación

1. Clona el repositorio:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd LibraryFastApi
    ```

2. Crea un entorno virtual y actívalo:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configura las variables de entorno:
    Copia el archivo `.env.example` a `.env` y actualiza los valores según tu configuración:

    ```bash
    cp .env.example .env
    ```

## Ejecución

1. Inicia la aplicación:

    ```bash
    uvicorn main:app --reload
    ```

2. La API estará disponible en `http://127.0.0.1:8000`.

## Endpoints

### Autenticación

- `POST /v1/auth/create`: Crear un nuevo usuario.
- `POST /v1/auth/token`: Obtener un token de acceso.
- `GET /v1/auth/user`: Obtener todos los usuarios (solo ADMIN).
- `GET /v1/auth/user/current`: Obtener el usuario actual.
- `PUT /v1/auth/user/password`: Cambiar la contraseña de un usuario (solo ADMIN).
- `PUT /v1/auth/user/phone_number`: Cambiar el número de teléfono de un usuario (solo ADMIN).
- `DELETE /v1/auth/delete/user`: Eliminar un usuario (solo ADMIN).

### Libros

- `GET /v1/book/`: Obtener todos los libros.
- `GET /v1/book/{book_id}`: Obtener un libro por ID.
- `POST /v1/book/create_book/`: Crear un nuevo libro.
- `PUT /v1/book/{book_id}/update`: Actualizar un libro por ID.
- `DELETE /v1/book/{book_id}/delete`: Eliminar un libro por ID.

## Modelos

### BookModel

- `id`: Integer, primary key.
- `title`: String.
- `description`: String.
- `priority`: Integer.
- `complete`: Boolean, default False.

### UserModel

- `id`: Integer, primary key.
- `email`: String, unique.
- `username`: String, unique.
- `first_name`: String.
- `last_name`: String.
- `password`: String.
- `is_active`: Boolean, default True.
- `role`: String.
- `phone_number`: String.
