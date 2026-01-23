from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.errors.messages import NOT_FOUND_ERROR
from app.genres.crud import fetch_genre_by_id
from app.genres.models import Genre


def get_genre(genre_id: int, db: Session = Depends(get_db)) -> type[Genre]:
    genre = fetch_genre_by_id(db, genre_id)
    if not genre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=NOT_FOUND_ERROR,
        )

    return genre
