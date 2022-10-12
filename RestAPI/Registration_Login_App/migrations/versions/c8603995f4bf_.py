"""empty message

Revision ID: c8603995f4bf
Revises: c67b12544d75
Create Date: 2022-09-08 06:55:49.477226

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c8603995f4bf'
down_revision = 'c67b12544d75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', mysql.VARCHAR(length=80), nullable=False))
    # ### end Alembic commands ###