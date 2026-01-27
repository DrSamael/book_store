from datetime import date

from pydantic import BaseModel, ConfigDict
from typing import List

from app.schemas.shared import BookBaseSchema, GenreBaseSchema, WriterBaseSchema


class WriterCreateSchema(BaseModel):
    name: str
    bio: str | None = None
    birth_date: date | None = None
    death_date: date | None = None
    country: str | None = None
    genre_ids: List[int] = []
    book_ids: List[int] = []


class WriterResponseSchema(WriterBaseSchema):
    books: List[BookBaseSchema]
    genres: List[GenreBaseSchema]

    class Config:
        from_attributes = True


class WriterUpdateSchema(BaseModel):
    name: str | None = None
    bio: str | None = None
    birth_date: date | None = None
    death_date: date | None = None
    country: str | None = None
    genre_ids: List[int] | None = None
    book_ids: List[int] | None = None

    model_config = ConfigDict(extra="forbid")
