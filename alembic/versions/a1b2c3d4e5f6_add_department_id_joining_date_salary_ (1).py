"""add department_id, joining_date, salary back to users (safe/idempotent)

Revision ID: a1b2c3d4e5f6
Revises: afb998496cd3
Create Date: 2026-07-09 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect


# revision identifiers, used by Alembic.
revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, Sequence[str], None] = 'afb998496cd3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    bind = op.get_bind()
    inspector = inspect(bind)

    existing_columns = [col["name"] for col in inspector.get_columns("users")]
    existing_fks = [fk["name"] for fk in inspector.get_foreign_keys("users")]

    if "department_id" not in existing_columns:
        op.add_column("users", sa.Column("department_id", sa.Integer(), nullable=True))

    if "joining_date" not in existing_columns:
        op.add_column("users", sa.Column("joining_date", sa.Date(), nullable=True))

    if "salary" not in existing_columns:
        op.add_column("users", sa.Column("salary", sa.DECIMAL(10, 2), nullable=True))

    if "fk_users_department_id" not in existing_fks:
        op.create_foreign_key(
            "fk_users_department_id",
            "users",
            "departments",
            ["department_id"],
            ["id"]
        )


def downgrade() -> None:
    """Downgrade schema."""
    bind = op.get_bind()
    inspector = inspect(bind)

    existing_fks = [fk["name"] for fk in inspector.get_foreign_keys("users")]
    existing_columns = [col["name"] for col in inspector.get_columns("users")]

    if "fk_users_department_id" in existing_fks:
        op.drop_constraint("fk_users_department_id", "users", type_="foreignkey")

    if "salary" in existing_columns:
        op.drop_column("users", "salary")

    if "joining_date" in existing_columns:
        op.drop_column("users", "joining_date")

    if "department_id" in existing_columns:
        op.drop_column("users", "department_id")
