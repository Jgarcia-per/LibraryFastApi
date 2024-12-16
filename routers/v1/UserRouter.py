from fastapi import APIRouter
from starlette import status

from models.UserRequestModel import UserRequest
from models.UserModel import Users
from passlib.context import CryptContext
from configs.Database import db_dependency

AuthRouter = APIRouter()
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@AuthRouter.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: UserRequest):
    """
    Autenticate User
    """
    user_model = Users(**user_request.dict())
    user_model.password = bcrypt_context.hash(user_request.password)

    db.add(user_model)
    db.commit()
