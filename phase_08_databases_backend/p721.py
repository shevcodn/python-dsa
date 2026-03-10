from fastapi import FastAPI, WebSocketDisconnect, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()
connections: dict[str, WebSocket] = {}

@app.get("/")
async def get():
    return HTMLResponse("""
<html><body>
<input id="name" placeholder="Your name">
<button onclick="connect()">Connect</button><br><br>
<input id="msg" type="text" placeholder="Message">
<button onclick="ws.send(document.getElementById('msg').value)">Send</button>
<ul id="messages"></ul>
<script>
  var ws;
  function connect() {
    var name = document.getElementById('name').value;
    ws = new WebSocket("ws://localhost:8000/ws/" + name);
    ws.onmessage = function(e) {
      var li = document.createElement("li");
      li.textContent = e.data;
      document.getElementById("messages").appendChild(li);
    };
  }
</script>
</body></html>
""")

async def broadcast(message: str):
    for ws in connections.values():
        await ws.send_text(message)

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    connections[username] = websocket
    await broadcast(f"{username} joined the chat")
    try:
        while True:
            data = await websocket.receive_text()
            await broadcast(f"{username}: {data}")
    except WebSocketDisconnect:
        connections.pop(username, None)
        await broadcast(f"{username} left the chat")
