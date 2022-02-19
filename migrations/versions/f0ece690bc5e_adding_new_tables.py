"""adding new tables

Revision ID: f0ece690bc5e
Revises: ad228c2cf089
Create Date: 2020-04-21 15:02:12.454422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0ece690bc5e'
down_revision = 'ad228c2cf089'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('list_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('book_item', sa.Integer(), nullable=False),
    sa.Column('book_quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('list_item', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_list_item_id'), ['id'], unique=True)

    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=25), nullable=False),
    sa.Column('total', sa.DECIMAL(), nullable=False),
    sa.Column('promo_id', sa.Integer(), nullable=True),
    sa.Column('shipping_info', sa.String(length=75), nullable=True),
    sa.Column('card_num', sa.String(length=128), nullable=True),
    sa.Column('card_exp', sa.String(length=128), nullable=True),
    sa.Column('cardtype', sa.String(length=1), nullable=True),
    sa.Column('last_four', sa.String(length=4), nullable=True),
    sa.Column('confirmation_num', sa.Integer(), nullable=True),
    sa.Column('order_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('confirmation_num')
    )
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_order_id'), ['id'], unique=True)
        batch_op.create_index(batch_op.f('ix_order_order_date'), ['order_date'], unique=False)

    op.create_table('promotion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('promo_code', sa.String(length=12), nullable=False),
    sa.Column('percentage', sa.Float(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('promotion', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_promotion_id'), ['id'], unique=True)

    with op.batch_alter_table(u'book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('book_cover', sa.String(length=75), nullable=False))
        batch_op.add_column(sa.Column('buying_price', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('edition', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('isbn', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('publisher', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('selling_price', sa.Integer(), nullable=False))
        batch_op.create_index(batch_op.f('ix_book_isbn'), ['isbn'], unique=True)
        batch_op.drop_column('price')
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table(u'book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('price', sa.INTEGER(), nullable=False))
        batch_op.drop_index(batch_op.f('ix_book_isbn'))
        batch_op.drop_column('selling_price')
        batch_op.drop_column('publisher')
        batch_op.drop_column('isbn')
        batch_op.drop_column('edition')
        batch_op.drop_column('buying_price')
        batch_op.drop_column('book_cover')

    with op.batch_alter_table('promotion', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_promotion_id'))

    op.drop_table('promotion')
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_order_order_date'))
        batch_op.drop_index(batch_op.f('ix_order_id'))

    op.drop_table('order')
    with op.batch_alter_table('list_item', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_list_item_id'))

    op.drop_table('list_item')
    # ### end Alembic commands ###