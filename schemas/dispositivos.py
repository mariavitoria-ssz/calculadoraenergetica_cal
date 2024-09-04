from pydantic import BaseModel, Field
from typing import List

class DispositivoCreate(BaseModel):
    unidade_consumidora_id: int
    dependencia_id: int
    tipo_id: int
    nome: str
    consumo: float = Field(gt=0, description="Consumo do dispositivo em kWh")
    uso_diario: float = Field(ge=0, le=24, description="Uso diário do dispositivo em horas")

class DispositivoUpdate(BaseModel):
    nome: str
    consumo: float = Field(gt=0, description="Consumo do dispositivo em kWh")
    uso_diario: float = Field(ge=0, le=24, description="Uso diário do dispositivo em horas")
    tipo_id: int

class DispositivoRead(BaseModel):
    id: int
    unidade_consumidora_id: int
    dependencia_id: int
    tipo_id: int
    nome: str
    consumo: float
    uso_diario: float

class DispositivoReadMany(BaseModel):
    id: int
    nome: str
    tipo_id: int

class DispositivoReadList(BaseModel):
    dispositivos: List[DispositivoReadMany] = []
