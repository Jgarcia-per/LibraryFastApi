from test.services.test_UserService import override_get_current_user
from test.configs.test_Database import test_info_user, TestingSessionLocal
from fastapi.testclient import TestClient
from starlette import status
from services.UserService import get_current_user
from models.UserModel import Users
from main import app
from passlib.context import CryptContext

import logging

logging.basicConfig(level=logging.INFO)

app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def test_create_user(test_info_user):
    """
    Test the creation of a new user.
    """
    request_data={
        'username': 'New_User_Pytest',
        'email': 'New_User-in-pytest@example.com',
        'first_name': 'New_User',
        'last_name': 'Pytest',
        'password': 'NewPassWord',
        'role': 'ADMIN',
        'phone_number': '111 222 3344'
    }
    response = client.post("/v1/auth/create/", json=request_data)
    assert response.status_code == 201

    db = TestingSessionLocal()
    model = db.query(Users).filter(Users.id == 2).first()
    assert model.email == request_data.get('email')
    assert model.username == request_data.get('username')
    assert model.first_name == request_data.get('first_name')
    assert model.last_name == request_data.get('last_name')
    assert pwd_context.verify(request_data.get('password'), model.password)
    assert model.role == request_data.get('role')
    assert model.phone_number == request_data.get('phone_number')

def test_user_all(test_info_user):
    response = client.get("/v1/auth/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
                                    'email': 'user_pytest@gmail.com',
                                    'first_name': 'User',
                                    'id': 1,
                                    'is_active': True,
                                    'last_name': 'pytest',
                                    'password': 'AdminPassword',
                                    'phone_number': '999 888 7766',
                                    'role': 'ADMIN',
                                    'username': 'User Pytest'
                                }]

def test_change_password(test_info_user):
    request_data={
        'new_password': 'NewPassword',
        'user_id': '1'
    }
    response = client.put('/v1/auth/user/password', json=request_data)
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Users).filter(Users.id == 1).first()
    assert pwd_context.verify('NewPassword', model.password)

def test_change_password_not_found(test_info_user):
    request_data={
        'new_password': 'NewPassword',
        'user_id': '999'
    }
    response = client.put('/v1/auth/user/password', json=request_data)
    assert response.status_code == 404

def test_change_phoneNumber(test_info_user):
    request_data={
        'new_phone_number': '999 888 7777',
        'user_id': '1'
    }
    response = client.put('/v1/auth/user/phone_number', json=request_data)
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Users).filter(Users.id == 1).first()
    assert model.phone_number =='999 888 7777'

def test_change_phoneNumber_not_found(test_info_user):
    request_data={
        'new_phone_number': '999 888 7777',
        'user_id': '999'
    }
    response = client.put('/v1/auth/user/phone_number', json=request_data)
    assert response.status_code == 404

def test_delete_user(test_info_user):
    response = client.delete("/v1/auth/user/delete/1")
    assert response.status_code == 204

    db = TestingSessionLocal()
    model = db.query(Users).filter(Users.id == 1).first()
    assert model is None

def test_delete_user_not_found(test_info_user):
    response = client.delete("/v1/auth/user/delete/999")
    assert response.status_code == 404
