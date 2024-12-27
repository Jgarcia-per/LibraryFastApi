from pydantic import BaseModel, Field

class Token(BaseModel):
    access_token: str = Field(min_length=1)
    token_type: str = Field(min_length=1)
