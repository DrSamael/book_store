from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import JSONResponse

from app.api import api_router
# from app.config import get_settings


def get_application() -> FastAPI:
    # settings = get_settings()
    _app = FastAPI()

    # _app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=settings.allowed_cors_origin,
    #     allow_credentials=settings.allowed_cors_credentials,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )

    _app.include_router(api_router, prefix="/api/v1")

    @_app.get(
        "/api/v1/health",
        tags=["Health check end-points"],
    )
    async def health_check():
        return JSONResponse(status_code=200, content={"message": "Hello World"})

    return _app


app = get_application()
