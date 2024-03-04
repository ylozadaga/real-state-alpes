from fastapi import FastAPI
from company_data_auditor.config.api import app_configs #, settings
from company_data_auditor.api.v1.router import router as v1

from company_data_auditor.modulos.infraestructura.consumidores import suscribirse_a_topico
from company_data_auditor.modulos.infraestructura.v1.eventos import EventoCompanyAuditada, CompanyAuditada
from company_data_auditor.modulos.infraestructura.v1.comandos import ComandoAuditarCompany
from company_data_auditor.modulos.infraestructura.despachadores import Despachador
from company_data_auditor.seedwork.infraestructura import utils

import asyncio
import time
import traceback
import uvicorn

app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("evento-auditar-company", "sub-company-audited", EventoCompanyAuditada))
    task2 = asyncio.ensure_future(suscribirse_a_topico("comando-auditar-company", "sub-com-auditar-company", ComandoAuditarCompany))
    # task3 = asyncio.ensure_future(suscribirse_a_topico("comando-disable-company", "sub-com-disable-company", ComandoDesactivarCompany))
    tasks.append(task1)
    tasks.append(task2)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()

@app.get("/prueba-auditar-company", include_in_schema=False)
async def prueba_auditar_company() -> dict[str, str]:
    comando = ComandoAuditarCompany(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=CompanyAuditada.__name__,
        data = CompanyAuditada(id = "1232321321", fecha_audit = utils.time_millis())
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-auditar-company")
    return {"status": "ok"}

@app.get("/prueba-company-auditada", include_in_schema=False)
async def prueba_company_auditada() -> dict[str, str]:
    evento = EventoCompanyAuditada(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=CompanyAuditada.__name__,
        company_audited = CompanyAuditada(id = "1232321321", fecha_audit = utils.time_millis())
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-auditar-company")
    return {"status": "ok"}

@app.get("/health", include_in_schema=False)
async def health() -> dict[str, str]:
    return {"status": "ok"}

app.include_router(v1, prefix="/v1", tags=["Version 1"])
