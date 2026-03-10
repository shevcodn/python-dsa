from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

app = FastAPI()

users_router = APIRouter(prefix="/users", tags=["users"])
items_router = APIRouter(prefix="/items", tags=["items"])

class Item(BaseModel):
    title: str
    price: float

items_db = []

@users_router.get("/")
async def get_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

@users_router.get("/{user_id}")
async def get_user(user_id: int):
    return {"id": user_id, "name": f"User {user_id}"}

@items_router.get("/")
async def get_items():
    return items_db

@items_router.post("/")
async def create_item(item: Item):
    items_db.append(item)
    return item

app.include_router(users_router)
app.include_router(items_router)
