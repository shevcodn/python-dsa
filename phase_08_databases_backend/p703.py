from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/users/")
async def create_user(user: User):
    return {"message": f"User {user.name} created succsessfully!", "user": user}

class Item(BaseModel):
    title: str
    price: float
    in_stock: bool = True

@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"Item '{item.title}' created successfully!", "item": item}





