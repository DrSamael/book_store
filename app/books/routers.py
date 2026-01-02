from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.books.crud import add_book, fetch_all_books, fetch_book_by_id, update_book
from app.database.database import get_db
from app.books.schemas import BookResponseSchema, BookCreateSchema, BookUpdateSchema
from app.errors.messages import NOT_FOUND

router = APIRouter(prefix="/books", tags=["Books"])


@router.post(
    "/",
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
        book_id: int,
        db: Session = Depends(get_db)
):
    book = fetch_book_by_id(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=NOT_FOUND,
        )

    return book


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


@router.patch(
    "/{book_id}",
    response_model=BookResponseSchema,
    status_code=status.HTTP_200_OK,
    description="Update a book",
)
def edit_book(
        book_id: int,
        data: BookUpdateSchema,
        db: Session = Depends(get_db),
):
    book = fetch_book_by_id(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    return update_book(db, book, data.model_dump(exclude_unset=True))
