from typing import Optional
from pydantic import BaseModel, Field


class Book:
    """
    Class Book

    """
    book_id:int
    title: str
    author: str
    description:str
    rating: int
    published_date: int

    def __init__(self, book_id, title, author, description, rating, published_date):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    """
    Class BookRequest
    """
    book_id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length= 3)
    author: str = Field(min_length= 1)
    description:str = Field(min_length= 1, max_length= 100)
    rating: int = Field(ge= 0, le= 5)
    published_date: int = Field(ge= -3000, le=9999)

    model_config = {
        "json_schema_extra": {
            "example": {
                    "title": "A New Book",
                    "author": "Random Writer",
                    "description": "Book Description",
                    "rating": 2,
                    "published_date": 0
            }
        }
    }
