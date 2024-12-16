from fastapi import APIRouter
from models.UserRequestModel import UserRequest
from models.UserModel import Users
from passlib.context import CryptContext

AuthRouter = APIRouter()
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@AuthRouter.post("/create")
async def create_user(user_request: UserRequest):
    """
    Autenticate User
    """
    create_user_model = Users(**user_request.dict())
    create_user_model.password = bcrypt_context.hash(user_request.password)

    return {create_user_model}
