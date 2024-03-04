from __future__ import annotations

from dataclasses import dataclass
from ....seedwork.domain.events import DomainEvent


@dataclass
class CompanyCreated(DomainEvent):
    id_company: str = None
    event_status: str = None
    creation_date: str = None
