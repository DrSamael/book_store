from fastapi import HTTPException
from sqlalchemy.orm import Session, selectinload
from starlette import status

from app.books.models import Book
from app.genres.models import Genre
from app.writers.models import Writer


def add_book(db: Session, data: dict) -> Book:
    allowed_fields = set(Book.__table__.columns.keys())
    allowed_fields.discard("id")
    book_data = {k: v for k, v in data.items() if k in allowed_fields}

    book = Book(**book_data)

    genre_ids = data.get("genre_ids")
    if genre_ids:
        genres = db.query(Genre).filter(Genre.id.in_(genre_ids)).all()
        book.genres.extend(genres)

    writer_ids = data.get("writer_ids")
    if writer_ids:
        writers = db.query(Writer).filter(Writer.id.in_(writer_ids)).all()
        book.writers.extend(writers)

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


def update_book(db: Session, book: type[Book], data: dict) -> type[Book]:
    book_fields = set(Book.__table__.columns.keys())
    for key, value in data.items():
        if key in book_fields:
            setattr(book, key, value)

    if "writer_ids" in data:
        writers = (
            db.query(Writer)
            .filter(Writer.id.in_(data["writer_ids"]))
            .all()
        )
        book.writers = writers

    if "genre_ids" in data:
        genres = (
            db.query(Genre)
            .filter(Genre.id.in_(data["genre_ids"]))
            .all()
        )
        book.genres = genres

    db.commit()
    db.refresh(book)

    return book
