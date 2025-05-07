from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func;
from app.models.base import Base;

class UserInput(Base):
    __tablename__ = 'user_input';

    id = Column(Integer, primary_key=True, index=True);
    data_hora = Column(DateTime(timezone=True), server_default=func.now())
    nome_cliente = Column(String(100), nullable=False);
    numero_cte = Column(String(20), nullable=False);
    numero_fatura = Column(String(20), nullable=False);

    #cte_id = Column(Integer, ForeignKey('cte_info.id'), nullable=False);