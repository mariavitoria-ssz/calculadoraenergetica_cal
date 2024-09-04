from pydantic import BaseModel
from typing import List

class BandeiraCreate(BaseModel):
    nome: str
    tarifa: float

class BandeiraRead(BaseModel):
    id: int
    nome: str
    tarifa: float

class BandeiraUpdate(BaseModel):
    nome: str
    tarifa: float

class BandeiraReadList(BaseModel):
    bandeiras: List[BandeiraRead]
