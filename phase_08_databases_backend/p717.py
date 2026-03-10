from fastapi import FastAPI, Request

app = FastAPI()

items = [{"id": i, "title": f"Item {i}", "price": i * 10.0} for i in range(1, 21)]

@app.get("/items/")
async def read_items(page: int = 1, size: int = 5, min_price: float = None):
    start = (page - 1) * size
    end = start + size
    filtered_items = items
    if min_price is not None:
        filtered_items = [item for item in items if item["price"] >= min_price]
    return {"total": len(filtered_items), "page": page, "size": size, "items": filtered_items[start:end]}

