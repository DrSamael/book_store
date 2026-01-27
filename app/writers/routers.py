from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from app.database.database import get_db
from app.writers.crud import create_writer, fetch_all_writers, update_writer, delete_writer
from app.writers.dependecies import get_writer
from app.writers.models import Writer
from app.writers.schemas import WriterResponseSchema, WriterCreateSchema, WriterUpdateSchema

router = APIRouter(prefix="/writers", tags=["Writers"])


@router.post(
    "",
    response_model=WriterResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_writer_endpoint(
        data: WriterCreateSchema,
        db: Session = Depends(get_db),
):
    return create_writer(db, data.model_dump())


@router.get(
    "/{writer_id}",
    response_model=WriterResponseSchema,
    status_code=status.HTTP_200_OK,
    description="Get a writer by Id",
)
async def get_genre_by_id(
        writer: Writer = Depends(get_writer),
):
    return writer


@router.get(
    "",
    response_model=list[WriterResponseSchema],
    status_code=status.HTTP_200_OK,
    description="Get all writers",
)
async def get_all_writers(
        db: Session = Depends(get_db)
):
    return fetch_all_writers(db)


@router.patch(
    "/{writer_id}",
    response_model=WriterResponseSchema,
    status_code=status.HTTP_200_OK,
    description="Update a writer",
)
async def edit_writer(
        data: WriterUpdateSchema,
        writer: Writer = Depends(get_writer),
        db: Session = Depends(get_db),
):
    return update_writer(db, writer, data.model_dump(exclude_unset=True))


@router.delete(
    "/{writer_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_writer_endpoint(
        writer: Writer = Depends(get_writer),
        db: Session = Depends(get_db),
):
    delete_writer(db, writer)
