from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User{user_id}"}

@app.get("/items/{item_id}")
async def get_item(item_id: int, q: str = None):
    return {"item_id": item_id, "description": f"Item {item_id} description", "query": q}

@app.get("/search")
async def search(keyword: str, limit: int = 10):
    return {"keyword": keyword, "limit": limit, "results": [f"Result {i+1} for '{keyword}'" for i in range(limit)]}



