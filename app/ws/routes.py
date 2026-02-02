from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.ws.manager import manager

router = APIRouter(prefix="/ws")


@router.websocket("/books/{book_id}")
async def book_ws(websocket: WebSocket, book_id: int):
    await manager.connect(book_id, websocket)

    try:
        while True:
            await websocket.receive_text()  # тримаємо зʼєднання
    except WebSocketDisconnect:
        manager.disconnect(book_id, websocket)
