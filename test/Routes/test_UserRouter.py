from test.services.test_UserService import override_get_current_user
from test.configs.test_Database import test_info_user, TestingSessionLocal
from fastapi.testclient import TestClient
from starlette import status
from services.UserService import get_current_user
from models.UserModel import Users
from main import app

app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)

def test_create_book(test_info_user):
    request_data={
        "username": "New_User_Pytest",
        "email": "New_User-in-pytest@example.com",
        "first_name": "New_User",
        "last_name": "Pytest",
        "password": "NewPasswordDefault",
        "role": "ADMIN",
        "phone_number": "111 222 3344"
    }
    response = client.post('/v1/auth/create/', json=request_data)
    assert response.status_code == 201

    db = TestingSessionLocal()
    model = db.query(Users).filter(Users.id == 2).first()
    assert model.email == request_data.get('email')
    assert model.username == request_data.get('username')
    assert model.first_name == request_data.get('first_name')
    assert model.last_name == request_data.get('last_name')
    assert model.password == request_data.get('password')
    assert model.role == request_data.get('role')
    assert model.phone_number == request_data.get('phone_number')


# def test_read_all(test_info_user):
#     response = client.get('/v1/auth/user')
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == [{'complete': False,
#                                 'description': 'This is a book used in unit testing',
#                                 'id': 1,
#                                 'priority': 5,
#                                 'title': 'Books in Pytest'}]

# def test_read_book(test_info_user):
#     response = client.get('/v1/book/1')
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == {'complete': False,
#                                 'description': 'This is a book used in unit testing',
#                                 'id': 1,
#                                 'priority': 5,
#                                 'title': 'Books in Pytest'}

# def test_read_book_not_found(test_info_user):
#     response = client.get('/v1/book/999')
#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Not Found'}

# def test_create_book(test_info_user):
#     request_data={
#         'title': 'New Book for pytest',
#         'description': 'New book book used in unit testing',
#         'priority': 5,
#         'complete': False
#     }
#     response = client.post('/v1/book/create_book/', json=request_data)
#     assert response.status_code == 201

#     db = TestingSessionLocal()
#     model = db.query(Book).filter(Book.id == 2).first()
#     assert model.title == request_data.get('title')
#     assert model.description == request_data.get('description')
#     assert model.priority == request_data.get('priority')
#     assert model.complete == request_data.get('complete')

# def test_update_book(test_info_user):
#     rerequest_data={
#         'title': 'Update Book for pytest',
#         'description': 'Update book book used in unit testing',
#         'priority': 2,
#         'complete': True
#     }
#     response = client.put('/v1/book/1/update', json=rerequest_data)
#     assert response.status_code == 204
#     db = TestingSessionLocal()
#     model = db.query(Book).filter(Book.id == 1).first()
#     assert model.title == 'Update Book for pytest'
#     assert model.description == 'Update book book used in unit testing'
#     assert model.priority == 2
#     assert model.complete == True

# def test_update_book_not_found(test_info_user):
#     request_data={
#         'title': 'Update Book for pytest',
#         'description': 'Update book book used in unit testing',
#         'priority': 2,
#         'complete': True
#     }
#     response = client.put('/v1/book/999/update', json=request_data)
#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Not Found'}

# def test_delete_book(test_info_user):
#     response = client.delete('/v1/book/1/delete')
#     assert response.status_code == 204
#     db = TestingSessionLocal()
#     model = db.query(Book).filter(Book.id == 1).first()
#     assert model is None

# def test_delete_book_not_foun(test_info_user):
#     response = client.delete('/v1/book/999/delete')
#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Not Found'}
