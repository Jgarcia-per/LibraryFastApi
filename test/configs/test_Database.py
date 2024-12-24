from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from configs.Database import Base, get_db
from main import app
import pytest
from models.BookModel import Book
from models.UserModel import Users

SQLALCHEMY_DATABASE_URL = "sqlite:///./test/LibraryTest.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    """
    Start Test DataBase
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def test_info_book():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    book = Book(
        title = "Books in Pytest",
        description = "This is a book used in unit testing",
        priority = 5,
        complete = False,
    )

    db = TestingSessionLocal()
    db.add(book)
    db.commit()
    yield book
    db.close()

@pytest.fixture
def test_info_user():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    user = Users(
            email = 'user_pytest@gmail.com',
            username = 'User Pytest',
            first_name = 'User',
            last_name = 'pytest',
            password = '',
            is_active = True,
            role = 'ADMIN',
            phone_number = '999 888 7766'
    )

    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    db.close()
