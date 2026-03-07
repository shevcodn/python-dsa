def test_create(api_client, sample_user):
    response = api_client.post("/users", json=sample_user)
    assert response.status_code == 200
    assert response.json()["name"] == "Denis"

def test_get(api_client, sample_user):
    api_client.post("/users", json=sample_user)
    response = api_client.get("/users/1")
    assert response.json()["name"] == "Denis"

def test_not_found(api_client):
    response = api_client.get("/users/999")
    assert response.json() == {"error": "not found"}
