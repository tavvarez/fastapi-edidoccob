"""Criação da Tabela edi_generated

Revision ID: 00cd428550a5
Revises: 3deb1beee993
Create Date: 2025-05-07 11:00:40.756644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00cd428550a5'
down_revision: Union[str, None] = '3deb1beee993'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('edi_generated',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_geracao', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('nome_cliente', sa.String(length=100), nullable=False),
    sa.Column('caminho_arquivo', sa.String(length=255), nullable=False),
    sa.Column('user_input_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_input_id'], ['user_input.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_edi_generated_id'), 'edi_generated', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_edi_generated_id'), table_name='edi_generated')
    op.drop_table('edi_generated')
    # ### end Alembic commands ###
