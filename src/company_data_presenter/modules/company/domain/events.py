from __future__ import annotations

from dataclasses import dataclass, field
from ....seedwork.domain.events import (DomainEvent)
from datetime import datetime


@dataclass
class CompanyCreated(DomainEvent):
   id_company: str = None
   event_status: str = None
   creation_date: str = None
