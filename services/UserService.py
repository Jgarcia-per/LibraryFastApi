from datetime import datetime, timedelta, timezone
import jwt
from models.UserModel import Users
from passlib.context import CryptContext
from configs.variables import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user (username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user

def create_acces_token(username: str, user_id: int):
    encode = {"sub": username, "id": user_id}
    expires = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
