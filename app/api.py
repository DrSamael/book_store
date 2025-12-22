from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from app.books import routers as books_router


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
