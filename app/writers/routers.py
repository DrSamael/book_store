from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from app.database.database import get_db
from app.writers.crud import create_writer
from app.writers.schemas import WriterResponseSchema, WriterCreateSchema

router = APIRouter(prefix="/writers", tags=["Writers"])


@router.post(
    "/",
    response_model=WriterResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_writer_endpoint(
        data: WriterCreateSchema,
        db: Session = Depends(get_db),
):
    return create_writer(db, data.model_dump())
