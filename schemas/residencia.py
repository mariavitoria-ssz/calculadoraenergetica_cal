
from pydantic import BaseModel, Field

class ResidenciaCreate(BaseModel):
    proprietario: str

