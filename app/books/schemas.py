from pydantic import BaseModel, ConfigDict
from typing import List

from app.schemas.shared import WriterBaseSchema, GenreBaseSchema, BookBaseSchema


class BookCreateSchema(BaseModel):
    title: str
    writer_ids: List[int]
    genre_ids: List[int]


class BookResponseSchema(BookBaseSchema):
    writers: List[WriterBaseSchema]
    genres: List[GenreBaseSchema]

    class Config:
        from_attributes = True


class BookUpdateSchema(BaseModel):
    title: str | None = None
    writer_ids: List[int] | None = None
    genre_ids: List[int] | None = None

    model_config = ConfigDict(extra="forbid")
