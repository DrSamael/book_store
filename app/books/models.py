from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.associations.models import book_writer, book_genre
from app.database.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

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
