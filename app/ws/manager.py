from fastapi import WebSocket
from collections import defaultdict
from typing import Dict, List


class ConnectionManager:
    def __init__(self):
        self.rooms: Dict[int, List[WebSocket]] = defaultdict(list)

    async def connect(self, book_id: int, websocket: WebSocket):
        await websocket.accept()
        self.rooms[book_id].append(websocket)

    def disconnect(self, book_id: int, websocket: WebSocket):
        if websocket in self.rooms.get(book_id, []):
            self.rooms[book_id].remove(websocket)

            if not self.rooms[book_id]:
                del self.rooms[book_id]

    async def notify_book(self, book_id: int, payload: dict):
        for ws in self.rooms.get(book_id, []):
            await ws.send_json(payload)


manager = ConnectionManager()
