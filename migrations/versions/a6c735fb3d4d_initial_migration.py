"""Initial migration

Revision ID: a6c735fb3d4d
Revises: 
Create Date: 2025-07-17 18:30:08.687814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6c735fb3d4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('enclosures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('environment', sa.String(), nullable=True),
    sa.Column('open_to_visitors', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('zookeepers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('birthday', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('animals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.Column('zookeeper_id', sa.Integer(), nullable=True),
    sa.Column('enclosure_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enclosure_id'], ['enclosures.id'], ),
    sa.ForeignKeyConstraint(['zookeeper_id'], ['zookeepers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('animals')
    op.drop_table('zookeepers')
    op.drop_table('enclosures')
    # ### end Alembic commands ###
