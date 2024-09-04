from pydantic import BaseModel
from typing import List

class TipoDispositivoCreate(BaseModel):
    nome: str

class TipoDispositivoUpdate(BaseModel):
    nome: str

class TipoDispositivoRead(BaseModel):
    id: int
    nome: str

class TipoDispositivoReadList(BaseModel):
    tipos_dispositivos: List[TipoDispositivoRead]
