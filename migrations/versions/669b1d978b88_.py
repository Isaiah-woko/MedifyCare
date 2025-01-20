"""empty message

Revision ID: 669b1d978b88
Revises: 942908cdfa51
Create Date: 2025-01-20 09:49:42.611664

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '669b1d978b88'
down_revision = '942908cdfa51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('uploaded_file')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=108),
               type_=sa.String(length=255),
               existing_nullable=False)
        batch_op.alter_column('image_filename',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.String(length=150),
               existing_nullable=True)
        batch_op.drop_column('confirmed_at')
        batch_op.drop_column('image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', mysql.VARCHAR(length=150), nullable=True))
        batch_op.add_column(sa.Column('confirmed_at', mysql.DATETIME(), nullable=True))
        batch_op.alter_column('image_filename',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=108),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)

    op.create_table('uploaded_file',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('file_name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('uploader_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('timestamp', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['uploader_id'], ['user.id'], name='uploaded_file_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
