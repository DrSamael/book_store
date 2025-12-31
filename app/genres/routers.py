from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from app.database.database import get_db
from app.genres.crud import create_genre
from app.genres.schemas import GenreResponseSchema, GenreCreateSchema

router = APIRouter(prefix="/genres", tags=["Genres"])


@router.post(
    "/",
    response_model=GenreResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_genre_endpoint(
        data: GenreCreateSchema,
        db: Session = Depends(get_db),
):
    return create_genre(db, data.model_dump())
