from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()


def h(c):
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Chat</title>
        </head>
        <body>
            <h1>WebSocket Chat</h1>
            <h2>Your ID: <span id="ws-id"></span></h2>
            <form action="" onsubmit="sendMessage(event)">
                <input type="text" id="messageText" autocomplete="off"/>
                <button>Send</button>
            </form>
            <ul id='messages'>
            </ul>
            <script>    
                var client_id = 
    """+c+"""
    
                document.querySelector("#ws-id").textContent = client_id;
                var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages')
                    var message = document.createElement('li')
                    var content = document.createTextNode(event.data)
                    message.appendChild(content)
                    messages.appendChild(message)
                };
                function sendMessage(event) {
                    var input = document.getElementById("messageText")
                    ws.send(input.value)
                    input.value = ''
                    event.preventDefault()
                }
            </script>
        </body>
    </html>
    """
    return html


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

C = 0

@app.get("/")
async def get():
    global C
    C += 1
    html = h(str(C))
    return HTMLResponse(html)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        await manager.broadcast(f"Client {client_id}")  # When Client A connects, it sends its username "ClientA"
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client{client_id}: {data}")  # ClientA: Hello, everyone!
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client {client_id} left the chat")

