from pulsar.schema import *
from company_data_auditor.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from company_data_auditor.seedwork.infraestructura.utils import time_millis
import uuid

class AuditarCompany(Record):
    id = String()
    fecha_audit = Long()

class ComandoAuditarCompany(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ValidarUsuario")
    datacontenttype = String()
    service_name = String(default="company-auditor-pda")
    data = AuditarCompany

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
