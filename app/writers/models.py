from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.associations.models import writer_genre, book_writer
from app.database.database import Base


class Writer(Base):
    __tablename__ = "writers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship(
        "Book",
        secondary=book_writer,
        back_populates="writers",
    )

    genres = relationship(
        "Genre",
        secondary=writer_genre,
        back_populates="writers",
    )