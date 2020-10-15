"""add user model

Revision ID: 867067ce80e1
Revises: b98ee3841cdb
Create Date: 2020-10-15 17:26:02.831398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '867067ce80e1'
down_revision = 'b98ee3841cdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('packages', 'destination',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('packages', 'location',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('packages', 'origin',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('packages', 'recipient',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('packages', 'sender',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('packages', 'sender',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('packages', 'recipient',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('packages', 'origin',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('packages', 'location',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('packages', 'destination',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_table('users')
    # ### end Alembic commands ###
