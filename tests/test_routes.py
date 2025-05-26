from fastapi.testclient import TestClient
from fastapi import FastAPI
from app.api.routes import router  # Adjusted import path

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_health_route():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
