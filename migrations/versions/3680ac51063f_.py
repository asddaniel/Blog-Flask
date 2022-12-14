"""empty message

Revision ID: 3680ac51063f
Revises: 7442972806d2
Create Date: 2022-10-02 15:49:22.011945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3680ac51063f'
down_revision = '7442972806d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('articles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('photo', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='articles_pkey')
    )
    # ### end Alembic commands ###
