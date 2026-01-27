from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.orm import relationship

from app.associations.models import writer_genre, book_writer
from app.database.database import Base


class Writer(Base):
    __tablename__ = "writers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    bio = Column(Text, nullable=True)
    birth_date = Column(Date, nullable=True)
    death_date = Column(Date, nullable=True)
    country = Column(String(100), nullable=True)

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