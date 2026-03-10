from fastapi import FastAPI, WebSocketDisconnect, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

connections: list[WebSocket] = []

@app.get("/")
async def get():
    return HTMLResponse("""
<html><body>
<input id="msg" type="text">
<button onclick="ws.send(document.getElementById('msg').value)">Send</button>
<ul id="messages"></ul>
<script>
  var ws = new WebSocket("ws://localhost:8000/ws");
  ws.onmessage = function(e) {
    var li = document.createElement("li");
    li.textContent = e.data;
    document.getElementById("messages").appendChild(li);
  };
</script>
</body></html>
""")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for connection in connections:
                await connection.send_text(f"Broadcast: {data}")
    except WebSocketDisconnect:
        connections.remove(websocket)
