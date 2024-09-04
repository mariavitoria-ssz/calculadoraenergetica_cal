from pydantic import BaseModel
from typing import List
from schemas.dependencia import DependenciaReadMany

class UnidadeConsumidoraCreate(BaseModel):
    nome: str
    tipo_id: int

class UnidadeConsumidoraUpdate(BaseModel):
    nome: str

class UnidadeConsumidoraRead(BaseModel):
    id: int
    nome: str
    tipo_id: int
    dependencias: List[DependenciaReadMany]

class UnidadeConsumidoraReadForList(BaseModel):
    id: int
    nome: str
    tipo_id: int

class UnidadeConsumidoraReadList(BaseModel):
    unidades_consumidoras: List[UnidadeConsumidoraReadForList]
