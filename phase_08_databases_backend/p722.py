import os
import asyncio
import json
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from asyncpg import create_pool

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.pool = await create_pool(
        host="localhost", port=5432, database="learning", user="denis", password=os.getenv("DB_PASS", "password")
    )
    async with app.state.pool.acquire() as conn:
        await conn.execute("DROP TABLE IF EXISTS prices")
        await conn.execute("""
            CREATE TABLE prices (
                id SERIAL PRIMARY KEY,
                symbol TEXT NOT NULL,
                price REAL NOT NULL,
                updated_at TIMESTAMP DEFAULT NOW()
            )
        """)
        await conn.execute("INSERT INTO prices (symbol, price) VALUES ('AAPL', 189.0), ('TSLA', 245.0), ('BTC', 67000.0)")
    yield
    await app.state.pool.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def get():
    return HTMLResponse("""
<html><body>
<h3>Live Prices</h3>
<ul id="prices"></ul>
<script>
  var ws = new WebSocket("ws://localhost:8000/ws");
  ws.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var ul = document.getElementById("prices");
    ul.innerHTML = "";
    data.forEach(function(item) {
      var li = document.createElement("li");
      li.textContent = item.symbol + ": $" + item.price;
      ul.appendChild(li);
    });
  };
</script>
</body></html>
""")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            async with websocket.app.state.pool.acquire() as conn:
                rows = await conn.fetch("SELECT symbol, price FROM prices")
            data = json.dumps([{"symbol": r["symbol"], "price": r["price"]} for r in rows])
            await websocket.send_text(data)
            await asyncio.sleep(2)
    except Exception:
        pass
