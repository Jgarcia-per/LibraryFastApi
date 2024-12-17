from fastapi import FastAPI
from configs.Database import engine

from models import BookModel
from routers.v1.BookRouter import BookRouter

from models import UserModel
from routers.v1.UserRouter import AuthRouter


app = FastAPI()

BookModel.Base.metadata.create_all(bind=engine)
UserModel.Base.metadata.create_all(bind=engine)

app.include_router(AuthRouter, prefix="/v1/auth", tags=["auth"])
app.include_router(BookRouter, prefix="/v1/book", tags=["book"])
