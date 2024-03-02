"""Entidades del dominio de cliente

En este archivo usted encontrará las entidades del dominio de cliente

"""

from datetime import datetime
from company_data_auditor.seedwork.dominio.entidades import Entidad, AgregacionRaiz
from dataclasses import dataclass, field
#from .objetos_valor import Fechas

@dataclass
class Company(Entidad):
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

