from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from models.BookModel import Book
from configs.Database import db_dependency
from services.UserService import get_current_user

RoleRouter = APIRouter()
user_dependency = Annotated[dict, Depends(get_current_user)]

@RoleRouter.get("/test-role", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    """
    Get all Books
    """
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not login")
    if user.get('role') != "ADMIN":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User unauthorized check the role")
    return db.query(Book).all()
