"""drop sales_invoice_id

Revision ID: e1750f3d3fb9
Revises: 3d1ac764e4fe
Create Date: 2025-09-16 12:56:54.342496

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1750f3d3fb9'
down_revision: Union[str, Sequence[str], None] = '3d1ac764e4fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("sales_invoice_items", schema=None) as batch_op:
        batch_op.drop_column("sales_invoice_id")


def downgrade() -> None:
    with op.batch_alter_table("sales_invoice_items", schema=None) as batch_op:
        batch_op.add_column(sa.Column("sales_invoice_id", sa.Integer(), nullable=False))
        batch_op.create_foreign_key(
            "fk_sales_invoice_items_old_invoice",
            "sales_invoices",
            ["sales_invoice_id"],
            ["id"],
        )