from test.services.test_UserService import override_get_current_user
from fastapi.testclient import TestClient
from starlette import status
from services.UserService import get_current_user
from main import app

app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)

def test_read_all():
    response = client.get("/v1/book/")
    assert response.status_code == status.HTTP_200_OK
