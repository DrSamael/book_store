from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from app.books import routers as books_router
from app.genres import routers as genres_router
from app.writers import routers as writers_router
from app.books import websocket as websocket_router
from app.ws import routes as ws_router


class ErrorResponse(BaseModel):
    errors: dict


api_router = APIRouter(
    default_response_class=JSONResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        422: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)

api_router.include_router(books_router.router)
api_router.include_router(genres_router.router)
api_router.include_router(writers_router.router)
api_router.include_router(websocket_router.router)
api_router.include_router(ws_router.router)
