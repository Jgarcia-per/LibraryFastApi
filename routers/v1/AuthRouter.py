from fastapi import APIRouter

AuthRouter = APIRouter()

@AuthRouter.get("/user/")
async def get_user():
    """
    Autenticate User
    """
    return {'user': 'autenticated'}
