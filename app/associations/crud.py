from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.books.models import Book
from app.genres.models import Genre
from app.writers.models import Writer
from app.errors.messages import BOOKS_NOT_FOUND, GENRES_NOT_FOUND, WRITERS_NOT_FOUND


def get_books_by_ids(db: Session, book_ids: list):
    books = (
        db.query(Book)
        .filter(Book.id.in_(book_ids))
        .all()
    )
    if len(books) != len(book_ids):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=BOOKS_NOT_FOUND)

    return books


def get_genres_by_ids(db: Session, genre_ids: list):
    genres = (
        db.query(Genre)
        .filter(Genre.id.in_(genre_ids))
        .all()
    )
    if len(genres) != len(genre_ids):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=GENRES_NOT_FOUND)

    return genres


def get_writers_by_ids(db: Session, writer_ids: list):
    writers = (
        db.query(Writer)
        .filter(Writer.id.in_(writer_ids))
        .all()
    )
    if len(writers) != len(writer_ids):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=WRITERS_NOT_FOUND)

    return writers
