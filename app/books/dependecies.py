from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload

from app.books.crud import fetch_book_by_id
from app.books.models import Book
from app.database.database import get_db
from app.errors.messages import NOT_FOUND


def get_book(book_id: int, db: Session = Depends(get_db)) -> type[Book]:
    book = fetch_book_by_id(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=NOT_FOUND,
        )

    return book
