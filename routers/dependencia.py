from fastapi import APIRouter, HTTPException
from models.dependencia import DependenciaDB, UnidadeConsumidoraDB
from schemas.dependencia import (
    DependenciaCreate,
    DependenciaReadList,
    DependenciaReadOne,
    DependenciaUpdate
)

router = APIRouter(prefix='/dependencias', tags=['DEPENDÊNCIAS'])

@router.post('', response_model=DependenciaReadOne)
def criar_dependencia(novo_dependencia: DependenciaCreate):
    dependencia = DependenciaDB.create(**novo_dependencia.dict())
    return dependencia

@router.get('/unidade-consumidora/{unidade_consumidora_id}', response_model=DependenciaReadList)
def listar_dependencia_da_unidade_consumidora(unidade_consumidora_id: int):
    unidade_consumidora = UnidadeConsumidoraDB.get_or_none(UnidadeConsumidoraDB.id == unidade_consumidora_id)
    if unidade_consumidora is None:
        raise HTTPException(status_code=404, detail="Unidade Consumidora não encontrada")
    dependencias = DependenciaDB.select().where(DependenciaDB.unidade_consumidora == unidade_consumidora)
    return {'dependencias': dependencias}

@router.get('/{dependencia_id}', response_model=DependenciaReadOne)
def listar_dependencia(dependencia_id: int):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    if dependencia is None:
        raise HTTPException(status_code=404, detail="Dependência não encontrada")
    return dependencia

@router.patch('/{dependencia_id}', response_model=DependenciaReadOne)
def atualizar_dependencia(dependencia_id: int, novo_dependencia: DependenciaUpdate):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    if dependencia is None:
        raise HTTPException(status_code=404, detail="Dependência não encontrada")
    dependencia.nome = novo_dependencia.nome
    dependencia.save()
    return dependencia

@router.delete('/{dependencia_id}', response_model=DependenciaReadOne)
def excluir_dependencia(dependencia_id: int):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    if dependencia is None:
        raise HTTPException(status_code=404, detail="Dependência não encontrada")
    dependencia.delete_instance()
    return dependencia
