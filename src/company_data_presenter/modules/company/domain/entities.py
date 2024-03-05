from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass, field

from ....seedwork.domain.entities import RootAggregation
from ....modules.company.domain.events import CompanyCreated


@dataclass
class Company(RootAggregation):
    event_status: str = field(default="PENDING")
    nit: str = field(default_factory=str)
    acronym: str = field(default_factory=str)
    status: str = field(default_factory=str)
    validity: str = field(default_factory=str)
    organization_type: str = field(default_factory=str)
    registration_category: str = field(default_factory=str)

    def create_company(self):
        self.add_event(CompanyCreated(
            id_company=str(self.id),
            event_status="IN_PROGRESS",
            creation_date=datetime.now().isoformat()
        ))
