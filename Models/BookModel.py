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
