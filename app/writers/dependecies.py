from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.errors.messages import NOT_FOUND_ERROR
from app.writers.crud import fetch_writer_by_id
from app.writers.models import Writer


def get_writer(writer_id: int, db: Session = Depends(get_db)) -> type[Writer]:
    writer = fetch_writer_by_id(db, writer_id)
    if not writer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=NOT_FOUND_ERROR,
        )

    return writer
