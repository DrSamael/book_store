from alembic.util import status
from fastapi import HTTPException
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.exc import IntegrityError
from starlette import status

from app.associations.crud import get_books_by_ids, get_writers_by_ids
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


def fetch_all_genres(db: Session) -> list[type[Genre]]:
    return (
        db.query(Genre)
        .options(
            selectinload(Genre.writers),
            selectinload(Genre.books),
        )
        .all()
    )


def fetch_genre_by_id(db: Session, genre_id: int) -> type[Genre]:
    return (
        db.query(Genre)
        # .options(
        #     selectinload(Genre.writers),
        #     selectinload(Genre.books),
        # )
        .filter(Genre.id == genre_id)
        .first()
    )


def update_genre(db: Session, genre: Genre, data: dict):
    for key, value in data.items():
        setattr(genre, key, value)

    if "writer_ids" in data:
        writers = get_writers_by_ids(db, data.get("writer_ids"))
        genre.writers = writers

    if "book_ids" in data:
        books = get_books_by_ids(db, data.get("book_ids"))
        genre.books = books

    db.commit()
    db.refresh(genre)
    return genre


def delete_genre(db: Session, genre: Genre) -> None:
    db.delete(genre)
    db.commit()
