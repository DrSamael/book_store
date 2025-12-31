from pydantic import BaseModel
from typing import List

from app.schemas.shared import BookBaseSchema, GenreBaseSchema, WriterBaseSchema


class WriterCreateSchema(BaseModel):
    name: str
    genre_ids: List[int] = []


class WriterResponseSchema(WriterBaseSchema):
    books: List[BookBaseSchema]
    genres: List[GenreBaseSchema]

    class Config:
        from_attributes = True
