from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from config.database import shutdown_db, startup_db
from routers.bandeira import router as bandeira_router
from routers.dependencia import router as comodo_router
from routers.dispositivos import router as dispositivos_router
from routers.tipos_consumidor import router as tipo_router
from routers.tipos_dispositivos import router as tipos_dispositivos_router
from routers.unidade_consumidora import router as consumidor_router

app = FastAPI(title='CALCULADORA DE CONSUMO DE ENERGIA ELÉTRICA')


@app.get('/')
def read_root():
    return {"message": "API Suprema Conectada!"}


app.add_event_handler(event_type='startup', func=startup_db)
app.add_event_handler(event_type='shutdown', func=shutdown_db)

app.include_router(tipo_router)
app.include_router(consumidor_router)
app.include_router(comodo_router)
app.include_router(tipos_dispositivos_router)
app.include_router(dispositivos_router)
app.include_router(bandeira_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Função para calcular o consumo de energia de um dispositivo
def calcular_consumo(potencia_watts: float, horas_uso: float, tarifa_kwh: float):
    consumo_kwh = (potencia_watts * horas_uso) / 1000
    custo = consumo_kwh * tarifa_kwh
    return consumo_kwh, custo


# Definir o modelo para um dispositivo
class Dispositivo(BaseModel):
    potencia_watts: float
    horas_uso: float


# Definir o modelo para a requisição da residência
class CalculoResidenciaRequest(BaseModel):
    dispositivos: List[Dispositivo]
    tarifa_kwh: float


# Simulação de uma função que retorna dispositivos do banco de dados
def get_dispositivos_por_residencia(residenc_id: str):
    # Aqui você deve implementar a lógica para buscar os dispositivos do banco de dados
    # Exemplo fictício de retorno
    return [
        {"potencia_watts": 100, "horas_uso": 5},
        {"potencia_watts": 200, "horas_uso": 2},
    ]


# Endpoint para calcular o consumo de energia da residência
@app.post('/calcular-consumos/residencia/{residenc_id}')
def calcular_energia_residencia(residenc_id: str, request: CalculoResidenciaRequest):
    consumo_total = 0
    custo_total = 0

    # Obter os dispositivos da base de dados para a residência
    dispositivos = get_dispositivos_por_residencia(residenc_id)

    if dispositivos is None:
        raise HTTPException(status_code=404, detail="Dispositivos não encontrados para a residência fornecida.")

    # Calcular o consumo e custo total
    for dispositivo in dispositivos:
        consumo, custo = calcular_consumo(dispositivo['potencia_watts'], dispositivo['horas_uso'], request.tarifa_kwh)
        consumo_total += consumo
        custo_total += custo

    return {
        'consumo_total_kwh': consumo_total,
        'custo_total_reais': custo_total
    }
