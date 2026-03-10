from fastapi import FastAPI, Request, HTTPException, Depends
import redis.asyncio as redis

app = FastAPI()
redis_client = redis.from_url("redis://localhost:6379/0")

async def check_rate_limit(request: Request):
    ip = request.client.host
    get = await redis_client.get(f"rate:{ip}")
    count = int(get) if get else 0
    if count >= 5:
        raise HTTPException(status_code=429, detail="Too Many Requests")
    new_count = await redis_client.incr(f"rate:{ip}")
    if new_count == 1:
        await redis_client.expire(f"rate:{ip}", 60)
    return ip

@app.get("/")
async def root(ip: str = Depends(check_rate_limit)):
    return {"message": "OK", "ip": ip}

@app.get("/limit-status")
async def limit_status(request: Request):
    ip = request.client.host
    count = await redis_client.get(f"rate:{ip}")
    return {"ip": ip, "requests": int(count) if count else 0, "limit": 5}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

