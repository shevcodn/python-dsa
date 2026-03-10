from fastapi import FastAPI, BackgroundTasks, HTTPException
import redis.asyncio as redis
import json, asyncio
from contextlib import asynccontextmanager
import uuid

redis_client = redis.from_url("redis://localhost:6379/0")
app = FastAPI()

async def process_task(task_id: str, data: dict):
    await asyncio.sleep(5)
    result = {f"task: {task_id}": f"Processed data: {data}"}
    await redis_client.hset("task_results", task_id, json.dumps(result))
    await redis_client.hdel("task_data", task_id)
    await redis_client.lrem("task_queue", 0, task_id)
    expire_time = 300
    await redis_client.expire("task_results", expire_time)

@app.post("/tasks")
async def create_task(data: dict, background_tasks: BackgroundTasks):
    task_id = str(await redis_client.incr("task_id"))
    await redis_client.hset("task_data", task_id, json.dumps(data))
    await redis_client.rpush("task_queue", task_id)
    background_tasks.add_task(process_task, task_id, data)
    return {"task_id": task_id, "status": "queued"}

@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    result = await redis_client.hget("task_results", task_id)
    if result:
        return {"task_id": task_id, "status": "done", "result": json.loads(result)}
    data = await redis_client.hget("task_data", task_id)
    if data:
        return {"task_id": task_id, "status": "processing", "data": json.loads(data)}
    raise HTTPException(status_code=404, detail="Task not found")
