from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func;
from app.models.base import Base;

class EdiGenerated(Base):
    __tablename__ = "edi_generated";

    id = Column(Integer, primary_key=True, index=True);
    data_geracao = Column(DateTime(timezone=True), server_default=func.now());
    nome_cliente = Column(String(100), nullable=False);
    caminho_arquivo = Column(String(255), nullable=False);
    user_input_id = Column(Integer, ForeignKey("user_input.id"), nullable=False);
