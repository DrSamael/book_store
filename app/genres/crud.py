from alembic.util import status
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from starlette import status

from app.errors.messages import GENRE_DUPLICATE_ERROR
from app.genres.models import Genre


def create_genre(db: Session, data: dict) -> Genre:
    genre = Genre(**data)

    db.add(genre)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=GENRE_DUPLICATE_ERROR,
        )

    db.refresh(genre)
    return genre

# def update_genre(db: Session, genre: Genre, data: GenreUpdate):
#     for key, value in data.model_dump(exclude_unset=True).items():
#         setattr(genre, key, value)
#
#     db.commit()
#     db.refresh(genre)
#     return genre
