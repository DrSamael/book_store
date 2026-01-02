from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from app.books.crud import create_book, fetch_all_books
from app.database.database import get_db
from app.books.schemas import BookResponseSchema, BookCreateSchema

router = APIRouter(prefix="/books", tags=["Books"])


@router.post(
    "/",
    response_model=BookResponseSchema,
    status_code=status.HTTP_201_CREATED,
    description="Create a new book",
)
async def create_book_endpoint(
        data: BookCreateSchema,
        db: Session = Depends(get_db),
):
    return create_book(db, data.model_dump())


@router.get(
    "/",
    response_model=list[BookResponseSchema],
    status_code=status.HTTP_200_OK,
    description="Get all books",
)
async def get_all_books(
        db: Session = Depends(get_db)
):
    return fetch_all_books(db)
