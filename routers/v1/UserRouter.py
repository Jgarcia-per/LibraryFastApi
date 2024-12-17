from typing import Annotated
from starlette import status
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.UserRequestModel import UserRequest
from models.UserModel import Users
from models.TokenModel import Token
from configs.Database import db_dependency
from services.UserService import bcrypt_context, authenticate_user, create_acces_token

AuthRouter = APIRouter()

@AuthRouter.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: UserRequest):
    """
    Create User
    """
    user_model = Users(**user_request.dict())
    user_model.password = bcrypt_context.hash(user_request.password)

    db.add(user_model)
    db.commit()

@AuthRouter.post("/token", response_model=Token ,status_code=status.HTTP_200_OK)
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
                                 db: db_dependency):
    """
    Autenticate User
    """
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=400, detail='Wrong User or Password')
    token = create_acces_token(user.username, user.id)
    return {"access_token": token, "token_type": "bearer"}
