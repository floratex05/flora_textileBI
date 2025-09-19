"""Fix sales_invoice_items schema - keep only invoice_id

Revision ID: 3d1ac764e4fe
Revises: d299a73bde30
Create Date: 2025-09-15 20:40:22.412769
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision: str = "3d1ac764e4fe"
down_revision: Union[str, Sequence[str], None] = "d299a73bde30"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Rebuild sales_invoice_items table with only invoice_id (SQLite-safe)."""

    # Define new schema
    with op.batch_alter_table("sales_invoice_items", recreate="always") as batch_op:
        batch_op.add_column(sa.Column("id", sa.Integer(), primary_key=True))
        batch_op.add_column(sa.Column("invoice_id", sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column("item_id", sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column("qty", sa.Float(), nullable=False))
        batch_op.add_column(sa.Column("rate", sa.Float(), nullable=False))
        batch_op.add_column(sa.Column("discount", sa.Float(), server_default="0"))
        batch_op.add_column(sa.Column("gst_rate", sa.Float(), server_default="0"))
        batch_op.add_column(sa.Column("line_total", sa.Float(), server_default="0"))

        # Foreign keys
        batch_op.create_foreign_key(
            "fk_sales_invoice_items_invoice",
            "sales_invoices",
            ["invoice_id"],
            ["id"],
        )
        batch_op.create_foreign_key(
            "fk_sales_invoice_items_item",
            "items",
            ["item_id"],
            ["id"],
        )


def downgrade() -> None:
    """Rebuild sales_invoice_items table back with sales_invoice_id."""

    with op.batch_alter_table("sales_invoice_items", recreate="always") as batch_op:
        batch_op.add_column(sa.Column("id", sa.Integer(), primary_key=True))
        batch_op.add_column(sa.Column("sales_invoice_id", sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column("item_id", sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column("qty", sa.Float(), nullable=False))
        batch_op.add_column(sa.Column("rate", sa.Float(), nullable=False))
        batch_op.add_column(sa.Column("discount", sa.Float(), server_default="0"))
        batch_op.add_column(sa.Column("gst_rate", sa.Float(), server_default="0"))
        batch_op.add_column(sa.Column("line_total", sa.Float(), server_default="0"))

        # Foreign keys
        batch_op.create_foreign_key(
            "fk_sales_invoice_items_old_invoice",
            "sales_invoices",
            ["sales_invoice_id"],
            ["id"],
        )
        batch_op.create_foreign_key(
            "fk_sales_invoice_items_item",
            "items",
            ["item_id"],
            ["id"],
        )
