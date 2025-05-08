from pydantic import BaseModel;
from datetime import datetime;
from typing import Optional, List

class UserInputCreate(BaseModel):
    nome_cliente: str
    numero_fatura: str
    cte_ids: List[int]

class UserInputOut(BaseModel):
    id: int
    nome_cliente: str
    numero_fatura: str
    data_hora: datetime


    class Config:
        orm_mode = True