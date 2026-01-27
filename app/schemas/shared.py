from pydantic import BaseModel

from app.books.models import BookStatus


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

    class Config:
        from_attributes = True


class GenreBaseSchema(BaseModel):
    id: int
    name: str
    slug: str
    description: str | None = None

    class Config:
        from_attributes = True
