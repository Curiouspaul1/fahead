"""empty message

Revision ID: 919bffe8943a
Revises: a97879af32c1
Create Date: 2020-05-18 01:29:04.501196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '919bffe8943a'
down_revision = 'a97879af32c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    # ### end Alembic commands ###