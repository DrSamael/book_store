from sqlalchemy.orm import Session, selectinload
from sqlalchemy import or_

from app.associations.crud import get_genres_by_ids, get_writers_by_ids
from app.associations.models import book_genre, book_writer
from app.books.models import Book
from app.books.schemas import BookFilterSchema


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


def fetch_all_books(db: Session, filters: BookFilterSchema) -> list[type[Book]]:
    query = (
        db.query(Book)
        .options(
            selectinload(Book.writers),
            selectinload(Book.genres),
        )
    )

    # 🔍 search
    if filters.q:
        query = query.filter(
            or_(
                Book.title.ilike(f"%{filters.q}%"),
                Book.description.ilike(f"%{filters.q}%"),
            )
        )

    # 🎯 filters
    if filters.status:
        query = query.filter(Book.status == filters.status)

    if filters.published_year_from:
        query = query.filter(Book.published_year >= filters.published_year_from)

    if filters.published_year_to:
        query = query.filter(Book.published_year <= filters.published_year_to)

    if filters.rating_from:
        query = query.filter(Book.rating >= filters.rating_from)

    if filters.rating_to:
        query = query.filter(Book.rating <= filters.rating_to)

    # 🔗 genre filter (many-to-many)
    if filters.genre_id:
        genre_list = [genre.strip() for genre in filters.genre_id.split(",")]
        query = query.join(book_genre).filter(book_genre.c.genre_id.in_(genre_list))

    # 🔗 writer filter (many-to-many)
    if filters.writer_id:
        writer_list = [writer.strip() for writer in filters.writer_id.split(",")]
        query = query.join(book_writer).filter(book_writer.c.writer_id.in_(writer_list))

    # 📄 pagination
    offset = (filters.page - 1) * filters.page_size

    return (
        query
        .distinct()
        .offset(offset)
        .limit(filters.page_size)
        .all()
    )


def fetch_book_by_id(db: Session, book_id: int) -> type[Book]:
    return (
        db.query(Book)
        # .options(
        #     selectinload(Book.writers),
        #     selectinload(Book.genres),
        # )
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
