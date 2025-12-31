from pydantic import BaseModel


class BookBaseSchema(BaseModel):
    id: int
    title: str

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

    class Config:
        from_attributes = True
