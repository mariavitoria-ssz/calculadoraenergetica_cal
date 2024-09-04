from pydantic import BaseModel
from typing import List
from schemas.dispositivos import DispositivoReadMany

class DependenciaCreate(BaseModel):
    nome: str
    unidade_consumidora_id: int

class DependenciaUpdate(BaseModel):
    nome: str

class DependenciaReadOne(BaseModel):
    id: int
    unidade_consumidora_id: int
    nome: str
    dispositivos: List[DispositivoReadMany]

class DependenciaReadMany(BaseModel):
    id: int
    nome: str

class DependenciaReadManyWithDispositivos(BaseModel):
    id: int
    nome: str
    dispositivos: List[DispositivoReadMany]

class DependenciaReadList(BaseModel):
    dependencias: List[DependenciaReadManyWithDispositivos]
