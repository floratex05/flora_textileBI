"""Rename si_no to invoice_no

Revision ID: 53ce73508678
Revises: e1750f3d3fb9
Create Date: 2025-09-16 19:36:29.634582

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53ce73508678'
down_revision: Union[str, Sequence[str], None] = 'e1750f3d3fb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("sales_invoices") as batch_op:
        batch_op.alter_column("si_no", new_column_name="invoice_no")


def downgrade() -> None:
    with op.batch_alter_table("sales_invoices") as batch_op:
        batch_op.alter_column("invoice_no", new_column_name="si_no")
