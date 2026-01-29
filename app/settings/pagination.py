import math
from sqlalchemy.orm import Query
from pydantic.generics import GenericModel


def paginate(
        query: Query,
        page: int,
        size: int,
) -> dict:
    total = query.distinct().count()

    items = (
        query
        .offset((page - 1) * size)
        .limit(size)
        .all()
    )

    pages = math.ceil(total / size) if total else 1

    return {
        "items": items,
        "total": total,
        "page": page,
        "size": size,
        "pages": pages,
    }



