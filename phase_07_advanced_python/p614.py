import pytest
import httpx
import respx

BASE_URL = "https://api.example.com"

async def get_user(client, user_id):
    response = await client.get(f"{BASE_URL}/users/{user_id}")
    response.raise_for_status()
    return response.json()

async def create_user(client, name, email):
    response = await client.post(f"{BASE_URL}/users", json={"name": name, "email": email})
    response.raise_for_status()
    return response.json()

@pytest.mark.asyncio
@respx.mock
async def test_get_user():
    respx.get(f"{BASE_URL}/users/99").respond(404)
    async with httpx.AsyncClient() as client:
        with pytest.raises(httpx.HTTPStatusError):
            await get_user(client, 99)

@pytest.mark.asyncio
@respx.mock
async def test_create_user():
    respx.post(f"{BASE_URL}/users").respond(201, json={"id": 1, "name": "Pavel", "email": "pavel@example.com"})
    async with httpx.AsyncClient() as client:
        user = await create_user(client, "Pavel", "pavel@example.com")
        assert user["id"] == 1