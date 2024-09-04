
from pydantic import BaseModel, Field

class ComodoCreate(BaseModel):
    nome: str
    residencia_id: int

