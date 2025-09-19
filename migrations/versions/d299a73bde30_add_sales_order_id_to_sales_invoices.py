"""Add sales_order_id to sales_invoices (SQLite safe)

Revision ID: d299a73bde30
Revises: 
Create Date: 2025-09-14 15:15:07.480918
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "d299a73bde30"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema (SQLite batch mode)."""
    with op.batch_alter_table("sales_invoices", schema=None) as batch_op:
        batch_op.add_column(sa.Column("sales_order_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            "fk_sales_invoices_sales_order",
            "sales_orders",
            ["sales_order_id"],
            ["id"],
        )


def downgrade() -> None:
    """Downgrade schema (SQLite batch mode)."""
    with op.batch_alter_table("sales_invoices", schema=None) as batch_op:
        batch_op.drop_constraint("fk_sales_invoices_sales_order", type_="foreignkey")
        batch_op.drop_column("sales_order_id")
