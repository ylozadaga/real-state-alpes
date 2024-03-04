from pulsar.schema import *
from company_data_auditor.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from company_data_auditor.seedwork.infraestructura.utils import time_millis
import uuid

class CompanyAuditada(Record):
    id = String()
    fecha_audit = Long()

class EventoCompanyAuditada(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoCompanyAuditada")
    datacontenttype = String()
    service_name = String(default="company-auditor-pda")
    audited = CompanyAuditada

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

