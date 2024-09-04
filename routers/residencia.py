from fastapi import APIRouter

from schemas.residencia import ResidenciaCreate

router = APIRouter(prefix="/residencias",tags=["RESIDÊNCIAS"])

@router.post("/")
def criar_residencia(nova_residencia: ResidenciaCreate):
    return nova_residencia