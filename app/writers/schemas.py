from pydantic import BaseModel, ConfigDict
from typing import List

from app.schemas.shared import BookBaseSchema, GenreBaseSchema, WriterBaseSchema


class WriterCreateSchema(BaseModel):
    name: str
    genre_ids: List[int] = []
    book_ids: List[int] = []


class WriterResponseSchema(WriterBaseSchema):
    books: List[BookBaseSchema]
    genres: List[GenreBaseSchema]

    class Config:
        from_attributes = True


class WriterUpdateSchema(BaseModel):
    name: str | None = None
    genre_ids: List[int] | None = None
    book_ids: List[int] | None = None

    model_config = ConfigDict(extra="forbid")
