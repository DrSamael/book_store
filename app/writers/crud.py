from sqlalchemy.orm import Session

from app.genres.models import Genre
from app.writers.models import Writer


def create_writer(db: Session, data: dict) -> Writer:
    allowed_fields = set(Writer.__table__.columns.keys())
    allowed_fields.discard("id")
    writer_data = {k: v for k, v in data.items() if k in allowed_fields}

    writer = Writer(**writer_data)

    genre_ids = data.get("genre_ids")
    if genre_ids:
        genres = db.query(Genre).filter(Genre.id.in_(genre_ids)).all()
        writer.genres.extend(genres)

    db.add(writer)
    db.commit()
    db.refresh(writer)

    return writer
