from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from configs.Database import engine

from models import BookModel
from models import UserModel
from routers.v1.BookRouter import BookRouter
from routers.v1.UserRouter import AuthRouter



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

BookModel.Base.metadata.create_all(bind=engine)
UserModel.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app.include_router(AuthRouter, prefix='/v1/auth', tags=['auth'])
app.include_router(BookRouter, prefix='/v1/book', tags=['book'])

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
