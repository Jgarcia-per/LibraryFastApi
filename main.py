from fastapi import FastAPI
from models import BookModel
from configs.Database import engine

app = FastAPI()
BookModel.Base.metadata.create_all(bind=engine)
