from typing import Optional
from pydantic import BaseModel, Field


class Book:
    """
    Class Book

    """
    id:int
    title: str
    author: str
    description:str
    rating: int

    def __init__(self, book_id, title, author, description, rating):
        self.id = book_id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    """
    Class BookRequest
    """
    book_id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description:str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

    model_config = {
        "json_schema_extra": {
            "example": {
                    "title": "A New Book",
                    "author": "Random Writer",
                    "description": "Book Description",
                    "rating": 1
            }
        }
    }
