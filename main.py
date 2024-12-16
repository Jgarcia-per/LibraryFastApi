from fastapi import FastAPI

from routers.v1.AuthRouter import AuthRouter
from routers.v1.BookRouter import BookRouter

app = FastAPI()
app.include_router(AuthRouter, prefix="/v1/auth", tags=["auth"])
app.include_router(BookRouter, prefix="/v1/book", tags=["book"])
