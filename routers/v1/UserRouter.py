from typing import Annotated
from starlette import status
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.UserRequestModel import UserRequest
from models.UserModel import Users
from models.TokenModel import Token
from configs.Database import db_dependency
from services.UserService import bcrypt_context, authenticate_user, create_acces_token, get_current_user

AuthRouter = APIRouter()
user_dependency = Annotated[dict, Depends(get_current_user)]

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
    token = create_acces_token(user.username, user.role)
    return {"access_token": token, "token_type": "bearer"}

@AuthRouter.get("/test/role", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    """
    Get all Users
    """
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not login")
    if user.get('role') != "ADMIN":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User unauthorized check the role")
    return db.query(Users).all()

@AuthRouter.delete("/delete/user", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user: user_dependency, db: db_dependency, user_id: int):
    """
    Delete user
    """
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not login")
    if user.get('role') != "ADMIN":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User unauthorized check the role")
    user_model = db.query(Users).filter(Users.id == user_id).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail='Not Found')
    db.query(Users).filter(Users.id == user_id).delete()
    db.commit()
