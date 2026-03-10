from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = {1: {"title": "Laptop", "price": 1200.0}, 2: {"title": "Phone", "price": 800.0}}

class ItemUpdate(BaseModel):
    title: str | None = None
    price: float | None = None

class ItemPatch(BaseModel):
    title: str | None = None
    price: float | None = None

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemUpdate):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item.dict(exclude_unset=True)
    return items[item_id]

@app.patch("/items/{item_id}")
async def patch_item(item_id: int, item: ItemPatch):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    existing_item = items[item_id]
    updated_data = item.dict(exclude_unset=True)
    existing_item.update(updated_data)
    return existing_item

