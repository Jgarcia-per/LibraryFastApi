from fastapi import FastAPI
from models import TodosModel
from configs.Database import engine

app = FastAPI()
TodosModel.Base.metadata.create_all(bind=engine)
