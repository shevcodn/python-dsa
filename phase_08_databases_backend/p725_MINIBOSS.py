import os
import asyncio
import json
import redis.asyncio as redis
import asyncpg
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

redis_client = redis.from_url("redis://localhost:6379/0")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_client.ping()
    conn = await asyncpg.connect(host="localhost", port=5432, database="learning", user="denis", password=os.getenv("DB_PASS", "password"))
    await conn.execute("DROP TABLE IF EXISTS stocks")
    await conn.execute("CREATE TABLE stocks (symbol TEXT PRIMARY KEY, price REAL NOT NULL, updated_at TIMESTAMP DEFAULT NOW())")
    await conn.execute("INSERT INTO stocks (symbol, price) VALUES ('AAPL', 189.0), ('TSLA', 245.0), ('BTC', 67000.0)")
    await conn.close()
    yield
    await redis_client.aclose()

app = FastAPI(lifespan=lifespan)

async def get_prices():
    cached = await redis_client.get("stocks_cache")
    if cached:
        return json.loads(cached)
    conn = await asyncpg.connect(host="localhost", port=5432, database="learning", user="denis", password=os.getenv("DB_PASS", "password"))
    rows = await conn.fetch("SELECT symbol, price FROM stocks")
    await conn.close()
    data = [{"symbol": r["symbol"], "price": r["price"]} for r in rows]
    await redis_client.set("stocks_cache", json.dumps(data), ex=10)
    return data

@app.get("/")
async def root():
    return HTMLResponse("""
<html><body>
<h3>Live Stock Prices</h3>
<ul id="prices"></ul>
<script>
  var ws = new WebSocket("ws://localhost:8000/ws/prices");
  ws.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var ul = document.getElementById("prices");
    ul.innerHTML = "";
    data.forEach(function(s) {
      var li = document.createElement("li");
      li.textContent = s.symbol + ": $" + s.price;
      ul.appendChild(li);
    });
  };
</script>
</body></html>
""")

@app.get("/stocks")
async def get_stocks():
    cached = await redis_client.get("stocks_cache")
    if cached:
        return {"source": "cache", "data": json.loads(cached)}
    data = await get_prices()
    return {"source": "db", "data": data}

@app.post("/stocks/update")
async def update_stock(symbol: str, price: float):
    conn = await asyncpg.connect(host="localhost", port=5432, database="learning", user="denis", password=os.getenv("DB_PASS", "password"))
    await conn.execute("UPDATE stocks SET price = $1, updated_at = NOW() WHERE symbol = $2", price, symbol)
    await conn.close()
    await redis_client.delete("stocks_cache")
    return {"message": f"{symbol} updated to ${price}"}

@app.websocket("/ws/prices")
async def websocket_prices(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await get_prices()
            await websocket.send_text(json.dumps(data))
            await asyncio.sleep(3)
    except Exception:
        pass
