from typing import List

from pydantic import BaseModel, ConfigDict, Field

from app.books.models import BookStatus
from app.schemas.shared import WriterBaseSchema, GenreBaseSchema, BookBaseSchema


class BookCreateSchema(BaseModel):
    title: str
    isbn: str | None = None
    description: str | None = None
    published_year: int | None = None
    language: str | None = None
    pages: int | None = None
    rating: float | None = None
    cover_url: str | None = None
    status: BookStatus = BookStatus.draft
    writer_ids: List[int] = Field(..., min_items=1)
    genre_ids: List[int] = Field(..., min_items=1)


class BookResponseSchema(BookBaseSchema):
    writers: List[WriterBaseSchema]
    genres: List[GenreBaseSchema]

    class Config:
        from_attributes = True


class BookUpdateSchema(BaseModel):
    title: str | None = None
    isbn: str | None = None
    description: str | None = None
    published_year: int | None = None
    language: str | None = None
    pages: int | None = None
    rating: float | None = None
    cover_url: str | None = None
    status: BookStatus | None = None
    writer_ids: List[int] | None = None
    genre_ids: List[int] | None = None

    model_config = ConfigDict(extra="forbid")
