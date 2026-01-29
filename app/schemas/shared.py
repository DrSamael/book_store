from datetime import date
from typing import Generic, List, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

from app.books.models import BookStatus

T = TypeVar("T")


class BookBaseSchema(BaseModel):
    id: int
    title: str
    isbn: str | None = None
    description: str | None = None
    published_year: int | None = None
    language: str | None = None
    pages: int | None = None
    rating: float | None = None
    cover_url: str | None = None
    status: BookStatus

    class Config:
        from_attributes = True


class WriterBaseSchema(BaseModel):
    id: int
    name: str
    bio: str | None = None
    birth_date: date | None = None
    death_date: date | None = None
    country: str | None = None

    class Config:
        from_attributes = True


class GenreBaseSchema(BaseModel):
    id: int
    name: str
    slug: str
    description: str | None = None

    class Config:
        from_attributes = True


class PaginatedResponse(GenericModel, Generic[T]):
    items: List[T]

    total: int
    page: int
    size: int
    pages: int
