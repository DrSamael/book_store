from sqlalchemy.orm import Session, selectinload

from app.associations.crud import get_books_by_ids, get_genres_by_ids
from app.writers.models import Writer


def create_writer(db: Session, data: dict) -> Writer:
    allowed_fields = set(Writer.__table__.columns.keys())
    allowed_fields.discard("id")
    writer_data = {k: v for k, v in data.items() if k in allowed_fields}

    writer = Writer(**writer_data)

    if "genre_ids" in data:
        genres = get_genres_by_ids(db, data.get("genre_ids"))
        writer.genres = genres

    if "book_ids" in data:
        books = get_books_by_ids(db, data.get("book_ids"))
        writer.books.extend(books)

    db.add(writer)
    db.commit()
    db.refresh(writer)

    return writer


def fetch_all_writers(db: Session) -> list[type[Writer]]:
    return (
        db.query(Writer)
        .options(
            selectinload(Writer.genres),
            selectinload(Writer.books),
        )
        .all()
    )


def fetch_writer_by_id(db: Session, writer_id: int) -> type[Writer]:
    return (
        db.query(Writer)
        # .options(
        #     selectinload(Writer.genres),
        #     selectinload(Writer.books),
        # )
        .filter(Writer.id == writer_id)
        .first()
    )


def update_writer(db: Session, writer: Writer, data: dict):
    for key, value in data.items():
        setattr(writer, key, value)

    if "genre_ids" in data:
        genres = get_genres_by_ids(db, data.get("genre_ids"))
        writer.genres = genres

    if "book_ids" in data:
        books = get_books_by_ids(db, data.get("book_ids"))
        writer.books = books

    db.commit()
    db.refresh(writer)
    return writer


def delete_writer(db: Session, writer: Writer) -> None:
    db.delete(writer)
    db.commit()
