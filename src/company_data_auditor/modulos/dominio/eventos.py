from dataclasses import dataclass
from company_data_auditor.seedwork.dominio.eventos import EventoDominio
from datetime import datetime

@dataclass
class CompanyAuditada(EventoDominio):
    id: str = None
    registration_date: datetime = None
    renovation_date: datetime = None
    nit: str = None
    acronym: str = None
    status: str = None
    validity: str = None
    organization_type: str = None
    registration_category: str = None
    audit_date: datetime = None

