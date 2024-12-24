from test.services.test_UserService import override_get_current_user
from test.configs.test_Database import test_info_user, TestingSessionLocal
from fastapi.testclient import TestClient
from starlette import status
from services.UserService import get_current_user
from models.UserModel import Users
from main import app

app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)

def test_user_all(test_info_user):
    response = client.get("/v1/auth/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
                                    'email': 'user_pytest@gmail.com',
                                    'first_name': 'User',
                                    'id': 1,
                                    'is_active': True,
                                    'last_name': 'pytest',
                                    'password': '',
                                    'phone_number': '999 888 7766',
                                    'role': 'ADMIN',
                                    'username': 'User Pytest'
                                }]


# def test_create_user(test_info_user):
#     request_data={
#         'username': "New_User_Pytest",
#         "email": "New_User-in-pytest@example.com",
#         "first_name": "New_User",
#         "last_name": "Pytest",
#         "password": "NewPasswordDefault",
#         "role": "ADMIN",
#         "phone_number": "111 222 3344"
#     }
#     response = client.post('/v1/auth/create/', json=request_data)
#     assert response.status_code == 201

#     db = TestingSessionLocal()
#     model = db.query(Users).filter(Users.id == 2).first()
#     assert model.email == request_data.get('email')
#     assert model.username == request_data.get('username')
#     assert model.first_name == request_data.get('first_name')
#     assert model.last_name == request_data.get('last_name')
#     assert model.password == request_data.get('password')
#     assert model.role == request_data.get('role')
#     assert model.phone_number == request_data.get('phone_number')
