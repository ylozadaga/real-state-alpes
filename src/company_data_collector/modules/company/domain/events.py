from __future__ import annotations

from dataclasses import dataclass, field
from company_data_collector.seedwork.domain.events import (DomainEvent)
from datetime import datetime


@dataclass
class CompanyCreated(DomainEvent):
    id: str = None
    registration_date: datetime = None
    renovation_date: datetime = None
    nit: str = None
    acronym: str = None
    status: str = None
    validity: str = None
    organization_type: str = None
    registration_category: str = None
