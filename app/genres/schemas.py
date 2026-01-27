from typing import List

from pydantic import BaseModel, ConfigDict

from app.schemas.shared import GenreBaseSchema, BookBaseSchema, WriterBaseSchema


class GenreCreateSchema(BaseModel):
    name: str
    slug: str
    description: str | None = None


class GenreResponseSchema(GenreBaseSchema):
    books: List[BookBaseSchema]
    writers: List[WriterBaseSchema]

    class Config:
        from_attributes = True


class GenreUpdateSchema(BaseModel):
    name: str | None = None
    slug: str | None = None
    description: str | None = None
    writer_ids: List[int] | None = None
    book_ids: List[int] | None = None

    model_config = ConfigDict(extra="forbid")
