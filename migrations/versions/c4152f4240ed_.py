"""empty message

Revision ID: c4152f4240ed
Revises: 3f4d7cd8401f
Create Date: 2018-05-25 18:27:16.953305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4152f4240ed'
down_revision = '3f4d7cd8401f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('package', sa.Column('soft_deleted', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('package', 'soft_deleted')
    # ### end Alembic commands ###
