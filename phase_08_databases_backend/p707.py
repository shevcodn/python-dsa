import asyncio
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        print(f"{request.method} {request.url.path} — {process_time:.3f}s")
        return response

app.add_middleware(TimingMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/fast")
async def fast_endpoint():
    return {"message": "This is a fast endpoint!"}

@app.get("/slow")
async def slow_endpoint():
    await asyncio.sleep(0.5)
    return {"message": "This is a slow endpoint!"}
