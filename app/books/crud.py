from sqlalchemy.orm import Session, selectinload

from app.associations.crud import get_genres_by_ids, get_writers_by_ids
from app.books.models import Book


def add_book(db: Session, data: dict) -> Book:
    allowed_fields = set(Book.__table__.columns.keys())
    allowed_fields.discard("id")
    book_data = {k: v for k, v in data.items() if k in allowed_fields}
    book = Book(**book_data)

    writers = get_writers_by_ids(db, data.get("writer_ids"))
    book.writers.extend(writers)

    genres = get_genres_by_ids(db, data.get("genre_ids"))
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
        writers = get_writers_by_ids(db, data.get("writer_ids"))
        book.writers = writers

    if "genre_ids" in data:
        genres = get_genres_by_ids(db, data.get("genre_ids"))
        book.genres = genres

    db.commit()
    db.refresh(book)

    return book


def delete_book(db: Session, book: Book) -> None:
    db.delete(book)
    db.commit()
