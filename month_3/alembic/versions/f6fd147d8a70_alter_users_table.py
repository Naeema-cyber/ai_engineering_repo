"""alter users table

Revision ID: f6fd147d8a70
Revises: 
Create Date: 2025-10-27 09:41:44.240633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6fd147d8a70'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
    ALTER TABLE users
    ADD COLUMN gender ENUM('male', 'female', 'other') NOT NULL
    """)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
    ALTER TABLE users
    DROP COLUMN age""")
    pass


