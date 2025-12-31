from pydantic import BaseModel
from typing import List

from app.schemas.shared import WriterBaseSchema, GenreBaseSchema, BookBaseSchema


class BookCreateSchema(BaseModel):
    title: str
    writer_ids: List[int]
    genre_ids: List[int]


class BookResponse(BookBaseSchema):
    writers: List[WriterBaseSchema]
    genres: List[GenreBaseSchema]

    class Config:
        from_attributes = True
