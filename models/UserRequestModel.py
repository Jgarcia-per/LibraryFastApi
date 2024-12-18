from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    email: str = Field(pattern=r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b$')
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=8)
    role: str = Field(min_length=3, max_length=20)

class ChangePasswordRequest(BaseModel):
    new_password: str
    user_id: int