from pydantic import BaseModel
from typing import List

from app.schemas.shared import GenreBaseSchema, BookBaseSchema, WriterBaseSchema


class GenreCreateSchema(BaseModel):
    name: str


class GenreResponseSchema(GenreBaseSchema):
    books: List[BookBaseSchema]
    writers: List[WriterBaseSchema]

    class Config:
        from_attributes = True
