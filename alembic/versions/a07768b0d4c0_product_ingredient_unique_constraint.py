"""product_ingredient unique constraint

Revision ID: a07768b0d4c0
Revises: a80cd9a35e58
Create Date: 2017-05-18 11:39:52.258266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a07768b0d4c0'
down_revision = 'a80cd9a35e58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('_unique_name_unit', 'ingredient', ['name', 'unit'])
    op.create_unique_constraint(None, 'product', ['nappi_code'])
    op.add_column('product_ingredient', sa.Column('strength', sa.String(), nullable=True))
    op.create_unique_constraint('_unique_product_ingredient_strength', 'product_ingredient', ['product_id', 'ingredient_id', 'strength'])
    op.drop_column('product_ingredient', 'stength')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_ingredient', sa.Column('stength', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint('_unique_product_ingredient_strength', 'product_ingredient', type_='unique')
    op.drop_column('product_ingredient', 'strength')
    op.drop_constraint(None, 'product', type_='unique')
    op.drop_constraint('_unique_name_unit', 'ingredient', type_='unique')
    # ### end Alembic commands ###
