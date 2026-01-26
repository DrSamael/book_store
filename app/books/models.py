from enum import Enum as PyEnum

from sqlalchemy import Column, Integer, String, Text, Float, Enum
from sqlalchemy.orm import relationship

from app.associations.models import book_writer, book_genre
from app.database.database import Base


class BookStatus(str, PyEnum):
    draft = "draft"
    published = "published"
    archived = "archived"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    isbn = Column(String(20), unique=True, index=True, nullable=True)
    description = Column(Text, nullable=True)
    published_year = Column(Integer, nullable=True)
    language = Column(String(10), nullable=True)
    pages = Column(Integer, nullable=True)
    rating = Column(Float, nullable=True)
    cover_url = Column(String(512), nullable=True)
    status = Column(
        Enum(BookStatus, name="book_status"),
        nullable=False,
        default=BookStatus.draft,
        server_default=BookStatus.draft.value,
    )

    writers = relationship(
        "Writer",
        secondary=book_writer,
        back_populates="books",
    )

    genres = relationship(
        "Genre",
        secondary=book_genre,
        back_populates="books",
    )
