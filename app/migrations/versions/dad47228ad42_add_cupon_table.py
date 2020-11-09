"""add cupon table

Revision ID: dad47228ad42
Revises: edb298743631
Create Date: 2020-11-09 16:00:32.641589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dad47228ad42'
down_revision = 'edb298743631'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cupons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cupon_uuid', sa.String(), nullable=True),
    sa.Column('cupon_name', sa.String(), nullable=True),
    sa.Column('cupon_fee', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cupons')
    # ### end Alembic commands ###
