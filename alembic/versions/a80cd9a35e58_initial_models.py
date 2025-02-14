"""Initial models

Revision ID: a80cd9a35e58
Revises: 
Create Date: 2017-05-18 11:26:10.124764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a80cd9a35e58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('unit', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nappi_code', sa.String(), nullable=True),
    sa.Column('regno', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('schedule', sa.String(), nullable=True),
    sa.Column('dosage_form', sa.String(), nullable=True),
    sa.Column('pack_size', sa.Float(), nullable=True),
    sa.Column('is_generic', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_ingredient',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('stength', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredient.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('product_id', 'ingredient_id')
    )
    op.create_table('product_sep',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sep', sa.Float(), nullable=True),
    sa.Column('effective_date', sa.Date(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_sep')
    op.drop_table('product_ingredient')
    op.drop_table('product')
    op.drop_table('ingredient')
    # ### end Alembic commands ###
