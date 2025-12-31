from datetime import datetime, UTC
from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_settings


settings = get_settings()

print(settings.DATABASE_URI)
engine = create_engine(settings.DATABASE_URI, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

int_pk = Annotated[int, mapped_column(primary_key=True, index=True)]
created_at = Annotated[datetime, mapped_column(default=lambda: datetime.now(UTC))]
updated_at = Annotated[
    datetime,
    mapped_column(
        default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    ),
]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int_pk]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
