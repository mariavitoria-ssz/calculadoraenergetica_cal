from pydantic import BaseModel
from typing import List

class TipoConsumidorCreate(BaseModel):
    nome: str
    valor_kwh: float

class TipoConsumidorUpdate(BaseModel):
    nome: str
    valor_kwh: float

class TipoConsumidorRead(BaseModel):
    id: int
    nome: str
    valor_kwh: float

class TipoConsumidorReadList(BaseModel):
    tipos_consumidores: List[TipoConsumidorRead]
