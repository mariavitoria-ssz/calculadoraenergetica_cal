from fastapi import APIRouter

from schemas.comodos import ComodoCreate

router = APIRouter(prefix="/comodos",tags=["COMODOS"])

@router.post("/")
def criar_comodo(novo_comodo: ComodoCreate):
    return novo_comodo