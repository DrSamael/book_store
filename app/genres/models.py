from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.associations.models import book_genre, writer_genre
from app.database.database import Base

from app.books.models import Book
from app.writers.models import Writer


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    books = relationship(
        "Book",
        secondary=book_genre,
        back_populates="genres",
    )

    writers = relationship(
        "Writer",
        secondary=writer_genre,
        back_populates="genres",
    )
