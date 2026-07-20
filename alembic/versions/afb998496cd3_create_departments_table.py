"""create departments table

Revision ID: afb998496cd3
Revises: d673bbaa339e
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision = "afb998496cd3"
down_revision = "d673bbaa339e"
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        "departments",

        sa.Column("id", sa.Integer(), primary_key=True),

        sa.Column(
            "department_name",
            sa.String(100),
            nullable=False,
            unique=True
        ),

        sa.Column(
            "description",
            sa.Text(),
            nullable=True
        ),

        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default=sa.text("1")
        ),

        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP")
        ),

        sa.Column(
            "updated_at",
            sa.TIMESTAMP(),
            server_default=sa.text(
                "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"
            )
        )
    )


def downgrade():

    op.drop_table("departments")