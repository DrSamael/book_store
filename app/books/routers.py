from typing import Dict

from fastapi import Depends, APIRouter
# from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from starlette import status


router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


# @router.get(
#     "/",
#     response_model=CustomPage[CompaniesResponseSchema],
#     status_code=status.HTTP_200_OK,
# )
# async def get_admin_companies(
#     db: Session = Depends(get_db), query_params: CompanyQueryParamsSchema = Depends()
# ):
#     query = get_companies_by_type(CompanyTypes.dealer, query_params)
#     return paginate(db, query)
