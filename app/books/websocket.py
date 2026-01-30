from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(prefix="/ws", tags=["WebSockets"])

active_connections: list[WebSocket] = []


async def broadcast(message: str):
    for connection in active_connections:
        await connection.send_text(message)


@router.websocket("/books-example")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # send message to all
            await broadcast(data)
    except WebSocketDisconnect:
        active_connections.remove(websocket)
