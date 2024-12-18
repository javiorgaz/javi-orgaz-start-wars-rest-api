"""empty message

Revision ID: 34cc831f90cb
Revises: d421dc7f255d
Create Date: 2024-12-17 17:59:34.986736

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '34cc831f90cb'
down_revision = 'd421dc7f255d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.drop_column('biome')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('biome', postgresql.ENUM('Dessert', 'Forest', 'Frozen', 'Volcanic', name='biome_enum'), autoincrement=False, nullable=False))

    op.drop_table('cities')
    # ### end Alembic commands ###
