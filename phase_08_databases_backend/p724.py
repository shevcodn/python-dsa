import os
import json
import redis.asyncio as redis
import asyncpg
from contextlib import asynccontextmanager
from fastapi import FastAPI

redis_client = redis.from_url("redis://localhost:6379/0")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_client.ping()
    conn = await asyncpg.connect(host="localhost", port=5432, database="learning", user="denis", password=os.getenv("DB_PASS", "password"))
    await conn.execute("DROP TABLE IF EXISTS products")
    await conn.execute("CREATE TABLE products (id SERIAL PRIMARY KEY, name TEXT, price NUMERIC)")
    await conn.execute("INSERT INTO products (name, price) VALUES ('Laptop', 1200.0), ('Phone', 800.0), ('Tablet', 500.0), ('Watch', 300.0), ('Headphones', 150.0)")
    await conn.close()
    yield
    await redis_client.aclose()

app = FastAPI(lifespan=lifespan)

@app.get("/products")
async def get_products():
    cached = await redis_client.get("products_cache")
    if cached:
        return {"source": "cache", "data": json.loads(cached)}
    conn = await asyncpg.connect(host="localhost", port=5432, database="learning", user="denis", password=os.getenv("DB_PASS", "password"))
    rows = await conn.fetch("SELECT name, price FROM products")
    await conn.close()
    data = [{"name": r["name"], "price": float(r["price"])} for r in rows]
    await redis_client.set("products_cache", json.dumps(data), ex=30)
    return {"source": "db", "data": data}

@app.get("/cache/clear")
async def clear_cache():
    await redis_client.delete("products_cache")
    return {"message": "Cache cleared"}
