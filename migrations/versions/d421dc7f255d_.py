"""empty message

Revision ID: d421dc7f255d
Revises: 13d8c4ea9499
Create Date: 2024-12-17 12:49:10.133489

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd421dc7f255d'
down_revision = '13d8c4ea9499'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('biome',
               existing_type=postgresql.ENUM('Dessert', 'Forest', 'Frozen', 'Volcanic', name='biome_enum'),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('biome',
               existing_type=postgresql.ENUM('Dessert', 'Forest', 'Frozen', 'Volcanic', name='biome_enum'),
               nullable=True)

    # ### end Alembic commands ###
