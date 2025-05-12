from pydantic import BaseModel;
from datetime import datetime;

class EdiGeneratedOut(BaseModel):
    id: int;
    data_geracao: datetime;
    nome_cliente: str;
    caminho_arquivo: str;
    user_input_id: int;

    class Config:
        orm_mode = True;