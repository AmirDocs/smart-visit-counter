# tests FASTAPI endpoints

from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)

def test_home_route():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello visitor from {ip}! Thanks for stopping by." in response.text  

def test_create_item_route():
    response = client.post("/items/", json={"name": "Test item"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test item"
    assert "id" in data