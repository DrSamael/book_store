from sqlalchemy import Table, Column, ForeignKey

from app.database.database import Base

book_writer = Table(
    "book_writer",
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("writer_id", ForeignKey("writers.id"), primary_key=True),
)

book_genre = Table(
    "book_genre",
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("genre_id", ForeignKey("genres.id"), primary_key=True),
)

writer_genre = Table(
    "writer_genre",
    Base.metadata,
    Column("writer_id", ForeignKey("writers.id"), primary_key=True),
    Column("genre_id", ForeignKey("genres.id"), primary_key=True),
)
