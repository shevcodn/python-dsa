import redis.asyncio as redis
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException

redis_client = redis.from_url("redis://localhost:6379/0")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_client.ping()
    yield
    await redis_client.aclose()

app = FastAPI(lifespan=lifespan)

@app.get("/set")
async def set_value(key: str, value: str):
    await redis_client.set(key, value, ex=60)
    return {"key": key, "value": value}

@app.get("/get")
async def get_value(key: str):
    value = await redis_client.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value.decode()}

@app.get("/delete")
async def delete_value(key: str):
    result = await redis_client.delete(key)
    if result == 0:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"message": "Key deleted"}

@app.get("/keys")
async def list_keys():
    keys = await redis_client.keys("*")
    return {"keys": [key.decode() for key in keys]}
