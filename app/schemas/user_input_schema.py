from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserInputCreate(BaseModel):
    nome_cliente: str
    numero_fatura: str
    vencimento_fatura: int
    cte_ids: List[int]

class UserInputOut(BaseModel):
    id: int
    nome_cliente: str
    numero_fatura: str
    vencimento_fatura: int
    data_hora: datetime


    class Config:
        orm_mode = True