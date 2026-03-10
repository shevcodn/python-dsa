from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class UserIn(BaseModel):
    name: str
    email: str
    password: str

class UserOut(BaseModel):
    name: str
    email: str

@app.post("/users/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserIn):
    if user.email.endswith("@example.com"):
        raise HTTPException(status_code=400, detail="Email domain '@example.com' is not allowed")
    return UserOut(name=user.name, email=user.email)

class Item(BaseModel):
    id: int
    title: str
    price: float

@app.get("/items/{item_id}", response_model=list[Item])
async def get_items(item_id: int):
    items = [
        Item(id=1, title="Item 1", price=10.0),
        Item(id=2, title="Item 2", price=20.0),
        Item(id=3, title="Item 3", price=30.0)
    ]
    return [item for item in items if item.id == item_id]

