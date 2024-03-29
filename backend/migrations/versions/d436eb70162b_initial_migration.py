"""Initial migration.

Revision ID: d436eb70162b
Revises: 99e70004589f
Create Date: 2021-02-03 00:28:58.745921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd436eb70162b'
down_revision = '99e70004589f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team', sa.Column('nickname', sa.String(length=120), nullable=False))
    op.add_column('team', sa.Column('short_name', sa.String(length=10), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('team', 'short_name')
    op.drop_column('team', 'nickname')
    # ### end Alembic commands ###
