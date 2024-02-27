from __future__ import annotations
from dataclasses import dataclass, field
from src.company_data_collector.seedwork.domain.events import (DomainEvent)
from datetime import datetime


@dataclass
class CompanyCreated(DomainEvent):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
