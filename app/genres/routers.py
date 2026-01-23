from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from app.database.database import get_db
from app.genres.crud import create_genre, fetch_all_genres, update_genre, delete_genre
from app.genres.dependecies import get_genre
from app.genres.models import Genre
from app.genres.schemas import GenreResponseSchema, GenreCreateSchema, GenreUpdateSchema

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


@router.get(
    "/{genre_id}",
    response_model=GenreResponseSchema,
    status_code=status.HTTP_200_OK,
    description="Get a genre by Id",
)
async def get_genre_by_id(
        genre: Genre = Depends(get_genre),
):
    return genre


@router.get(
    "/",
    response_model=list[GenreResponseSchema],
    status_code=status.HTTP_200_OK,
    description="Get all genres",
)
async def get_all_genres(
        db: Session = Depends(get_db)
):
    return fetch_all_genres(db)


@router.patch(
    "/{genre_id}",
    response_model=GenreResponseSchema,
    status_code=status.HTTP_200_OK,
    description="Update a genre",
)
async def edit_genre(
        data: GenreUpdateSchema,
        genre: Genre = Depends(get_genre),
        db: Session = Depends(get_db),
):
    return update_genre(db, genre, data.model_dump(exclude_unset=True))


@router.delete(
    "/{genre_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_genre_endpoint(
        genre: Genre = Depends(get_genre),
        db: Session = Depends(get_db),
):
    delete_genre(db, genre)
