"""empty message

Revision ID: fe71661b0cd7
Revises: 
Create Date: 2017-04-19 11:37:59.869825

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'fe71661b0cd7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    users = op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
                    sa.Column('email', sa.String(length=128), nullable=False),
                    sa.Column('password', sa.String(length=128), nullable=False),
                    sa.Column('first_name', sa.String(length=128), nullable=False),
                    sa.Column('last_name', sa.String(length=128), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    posts = op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
                    sa.Column('user_id', sa.BIGINT(), nullable=False),
                    sa.Column('image_url', sa.String(length=256), nullable=False),
                    sa.Column('caption', sa.String(length=128), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_index(op.f('idx_users_email'), 'users', ['email'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('posts')
    # ### end Alembic commands ###