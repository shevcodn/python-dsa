import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
db = {}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in db:
        return {"error": "User not found"}, 404
    return db[user_id]

@app.post("/users")
def create_user(data: dict):
    user_id = len(db) + 1
    db[user_id] = data
    return {"id": user_id, **data}

@pytest.fixture
def client():
    db.clear()
    return TestClient(app)

def test_create_user(client):
    response = client.post("/users", json={"name": "Denis"})
    assert response.status_code == 200
    assert response.json()["name"] == "Denis"

def test_get_user(client):
    client.post("/users", json={"name": "Denis"})
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Denis"

    