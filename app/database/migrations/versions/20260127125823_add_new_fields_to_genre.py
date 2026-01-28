"""add new fields to genre

Revision ID: 20260127125823
Revises: 20260126195748
Create Date: 2026-01-27 12:58:24.890711

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20260127125823'
down_revision: Union[str, Sequence[str], None] = '20260126195748'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "genres",
        sa.Column("slug", sa.String(length=255), nullable=True),
    )

    op.execute("""
        UPDATE genres
        SET slug = lower(regexp_replace(name, '\\s+', '-', 'g')) || '-' || id
    """)

    op.alter_column("genres", "slug", nullable=False)
    # op.create_unique_constraint("uq_genres_slug", "genres", ["slug"])

    op.add_column(
        "genres",
        sa.Column("description", sa.Text(), nullable=True),
    )


def downgrade() -> None:
    # op.drop_constraint("uq_genres_slug", "genres", type_="unique")
    op.drop_column("genres", "description")
    op.drop_column("genres", "slug")
