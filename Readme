# LibraryFastApi

Este proyecto es una API simple creada con FastAPI. La API tiene un único endpoint que devuelve un mensaje de saludo.

## Estructura del Proyecto

```txt
/home/jgarcia/Personal/Cursos/Python/LibraryFastApi/
│
├── books.py
└── Readme.md
```

## books.py

El archivo `books.py` contiene la implementación de la API. Aquí está el contenido del archivo:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/api-endpoint")
async def first_api():
    return {"message": "Hello World"}
```

## Instalación

1. Clona el repositorio.
2. Navega al directorio del proyecto.
3. Instala las dependencias necesarias.

```bash
pip install fastapi uvicorn
```

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
uvicorn books:app --reload
```

La aplicación estará disponible en `http://127.0.0.1:8000`.

## Uso

Puedes acceder al endpoint de la API en `http://127.0.0.1:8000/api-endpoint` para recibir un mensaje de saludo.

```json
{
  "message": "Hello World"
}
```

## Contribución

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT.
