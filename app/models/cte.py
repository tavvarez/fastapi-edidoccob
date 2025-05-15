from sqlalchemy import Column, Integer, String, Numeric
from app.models.base import Base


class CteInfo(Base):
    __tablename__ = 'cte_info'

    id = Column(Integer, primary_key=True, index=True)
    data_emissao = Column(String(25), nullable=False)
    numero_cte = Column(Integer, nullable=False)
    serie_cte = Column(Integer)
    cnpj_cliente = Column(String(20))
    valor_receber = Column(Numeric(13, 2))
    valor_prestacao = Column(Numeric(13, 2))
    valor_mercadoria = Column(Numeric(13, 2))
    peso_mercadoria = Column(Numeric(13, 2))
    chave_nfe = Column(String(600))
    cnpj_destinatario = Column(String(20))
    nome_destinatario = Column(String(100))