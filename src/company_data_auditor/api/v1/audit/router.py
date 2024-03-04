from fastapi import APIRouter, status, BackgroundTasks
from company_data_auditor.modulos.aplicacion.comandos.auditar_company import ComandoAuditarCompany
from company_data_auditor.seedwork.presentacion.dto import RespuestaAsincrona
from company_data_auditor.seedwork.aplicacion.comandos import ejecutar_commando
#from company_data_auditor.seedwork.aplicacion.queries import ejecutar_query

from .dto import AuditCompany

router = APIRouter()

@router.post("/auditar", status_code=status.HTTP_202_ACCEPTED, response_model=RespuestaAsincrona)
async def audit_company(company: AuditCompany, background_tasks: BackgroundTasks) -> dict[str, str]:
    comando = ComandoAuditarCompany(
        id=company.id,
        registration_date=company.registration_date,
        renovation_date=company.renovation_date,
        nit=company.nit,
        acronym=company.acronym,
        status=company.status,
        validity=company.validity,
        organization_type=company.organization_type,
        registration_category=company.registration_category
        )
    background_tasks.add_task(ejecutar_commando, comando)
    return RespuestaAsincrona(mensaje="Company audit in process")
