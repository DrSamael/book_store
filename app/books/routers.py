from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from app.books.crud import add_book, fetch_all_books, update_book, delete_book
from app.books.dependecies import get_book
from app.books.models import Book
from app.database.database import get_db
from app.books.schemas import BookResponseSchema, BookCreateSchema, BookUpdateSchema

router = APIRouter(prefix="/books", tags=["Books"])


@router.post(
    "",
    response_model=BookResponseSchema,
    status_code=status.HTTP_201_CREATED,
    description="Create a new book",
)
async def create_book(
        data: BookCreateSchema,
        db: Session = Depends(get_db),
):
    return add_book(db, data.model_dump())


@router.get(
    "/{book_id}",
    response_model=BookResponseSchema,
    status_code=status.HTTP_200_OK,
    description="Get a books by Id",
)
async def get_book_by_id(
        book: Book = Depends(get_book),
):
    return book


@router.get(
    "",
    response_model=list[BookResponseSchema],
    status_code=status.HTTP_200_OK,
    description="Get all books",
)
async def get_all_books(
        db: Session = Depends(get_db)
):
    return fetch_all_books(db)


@router.patch(
    "/{book_id}",
    response_model=BookResponseSchema,
    status_code=status.HTTP_200_OK,
    description="Update a book",
)
async def edit_book(
        data: BookUpdateSchema,
        book: Book = Depends(get_book),
        db: Session = Depends(get_db),
):
    return update_book(db, book, data.model_dump(exclude_unset=True))


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_book_endpoint(
        book: Book = Depends(get_book_by_id),
        db: Session = Depends(get_db),
):
    delete_book(db, book)
