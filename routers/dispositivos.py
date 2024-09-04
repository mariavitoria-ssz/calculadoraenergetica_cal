from fastapi import APIRouter, HTTPException
from models.dependencia import DependenciaDB
from models.dispositivo import DispositivoDB
from models.unidade_consumidora import UnidadeConsumidoraDB
from schemas.dispositivos import (
    DispositivoCreate,
    DispositivoRead,
    DispositivoReadList,
    DispositivoUpdate
)

router = APIRouter(prefix='/dispositivos', tags=['DISPOSITIVOS'])

@router.post('', response_model=DispositivoRead)
def criar_dispositivo(novo_dispositivo: DispositivoCreate):
    dispositivo = DispositivoDB.create(**novo_dispositivo.dict())
    return dispositivo

@router.get('/unidades-consumidoras/{unidade_consumidora_id}', response_model=DispositivoReadList)
def listar_dispositivos_por_unidade(unidade_consumidora_id: int):
    unidade_consumidora = UnidadeConsumidoraDB.get_or_none(UnidadeConsumidoraDB.id == unidade_consumidora_id)
    if not unidade_consumidora:
        raise HTTPException(status_code=404, detail="Unidade Consumidora não encontrada")
    dispositivos = DispositivoDB.select().where(DispositivoDB.unidade_consumidora == unidade_consumidora)
    return {'dispositivos': dispositivos}

@router.get('/dependencias/{dependencia_id}', response_model=DispositivoReadList)
def listar_dispositivos_por_dependencia(dependencia_id: int):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    if not dependencia:
        raise HTTPException(status_code=404, detail="Dependência não encontrada")
    dispositivos = DispositivoDB.select().where(DispositivoDB.dependencia == dependencia)
    return {'dispositivos': dispositivos}

@router.get('/{dispositivo_id}', response_model=DispositivoRead)
def listar_dispositivo(dispositivo_id: int):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == dispositivo_id)
    if not dispositivo:
        raise HTTPException(status_code=404, detail="Dispositivo não encontrado")
    return dispositivo

@router.patch('/{dispositivo_id}', response_model=DispositivoRead)
def atualizar_dispositivo(dispositivo_id: int, dispositivo_atualizado: DispositivoUpdate):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == dispositivo_id)
    if not dispositivo:
        raise HTTPException(status_code=404, detail="Dispositivo não encontrado")
    dispositivo.nome = dispositivo_atualizado.nome
    dispositivo.consumo = dispositivo_atualizado.consumo
    dispositivo.uso_diario = dispositivo_atualizado.uso_diario
    dispositivo.tipo_id = dispositivo_atualizado.tipo_id
    dispositivo.save()
    return dispositivo

@router.delete('/{dispositivo_id}', response_model=DispositivoRead)
def eliminar_dispositivo(dispositivo_id: int):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == dispositivo_id)
    if not dispositivo:
        raise HTTPException(status_code=404, detail="Dispositivo não encontrado")
    dispositivo.delete_instance()
    return dispositivo
