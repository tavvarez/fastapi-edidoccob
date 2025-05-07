from pydantic import BaseModel;
from datetime import datetime;

class UserInputCreate(BaseModel):
    nome_cliente: str;
    numero_cte: str;
    numero_fatura: str;

class UserInputOut(UserInputCreate):
    id: int;
    data_hora: datetime;

    class Config:
        orm_mode = True;