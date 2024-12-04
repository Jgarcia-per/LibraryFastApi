# LibraryFastApi

Este proyecto es una API desarrollada con FastAPI para gestionar una biblioteca. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre libros y autores.

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn

## Instalación

1. Clona el repositorio:
  ```bash
  git clone https://github.com/tu_usuario/LibraryFastApi.git
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

## Uso

1. Inicia el servidor:
  ```bash
  uvicorn main:app --reload
  ```

2. Abre tu navegador y ve a `http://127.0.0.1:8000/docs` para ver la documentación interactiva de la API generada por Swagger.

## Endpoints

- `GET /books/` - Lista todos los libros
- `POST /books/` - Crea un nuevo libro
- `GET /books/{book_id}` - Obtiene un libro por ID
- `PUT /books/{book_id}` - Actualiza un libro por ID
- `DELETE /books/{book_id}` - Elimina un libro por ID
