"""add user model

Revision ID: 6643f9cd69f7
Revises: 867067ce80e1
Create Date: 2020-10-15 17:41:17.173418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6643f9cd69f7'
down_revision = '867067ce80e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('packages', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'packages', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'packages', type_='foreignkey')
    op.drop_column('packages', 'user_id')
    # ### end Alembic commands ###