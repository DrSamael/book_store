from fastapi import HTTPException
from sqlalchemy.orm import Session, selectinload
from starlette import status

from app.books.models import Book
from app.errors.messages import GENRES_NOT_FOUND, WRITERS_NOT_FOUND
from app.genres.models import Genre
from app.writers.models import Writer


def add_book(db: Session, data: dict) -> Book:
    allowed_fields = set(Book.__table__.columns.keys())
    allowed_fields.discard("id")
    book_data = {k: v for k, v in data.items() if k in allowed_fields}
    book = Book(**book_data)

    writers = _get_writers(db, data.get("writer_ids"))
    book.writers.extend(writers)

    genres = _get_genres(db, data.get("genre_ids"))
    book.genres.extend(genres)

    db.add(book)
    db.commit()
    db.refresh(book)

    return book


def fetch_all_books(db: Session) -> list[type[Book]]:
    return (
        db.query(Book)
        .options(
            selectinload(Book.writers),
            selectinload(Book.genres),
        )
        .all()
    )


def fetch_book_by_id(db: Session, book_id: int) -> type[Book]:
    return (
        db.query(Book)
        .options(
            selectinload(Book.writers),
            selectinload(Book.genres),
        )
        .filter(Book.id == book_id)
        .first()
    )


def update_book(db: Session, book: Book, data: dict) -> Book:
    book_fields = set(Book.__table__.columns.keys())
    for key, value in data.items():
        if key in book_fields:
            setattr(book, key, value)

    if "writer_ids" in data:
        writers = _get_writers(db, data.get("writer_ids"))
        book.writers = writers

    if "genre_ids" in data:
        genres = _get_genres(db, data.get("genre_ids"))
        book.genres = genres

    db.commit()
    db.refresh(book)

    return book


def delete_book(db: Session, book: Book) -> None:
    db.delete(book)
    db.commit()


def _get_genres(db: Session, genre_ids: list):
    genres = (
        db.query(Genre)
        .filter(Genre.id.in_(genre_ids))
        .all()
    )
    if len(genres) != len(genre_ids):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=GENRES_NOT_FOUND)

    return genres


def _get_writers(db: Session, writer_ids: list):
    writers = (
        db.query(Writer)
        .filter(Writer.id.in_(writer_ids))
        .all()
    )
    if len(writers) != len(writer_ids):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=WRITERS_NOT_FOUND)

    return writers
