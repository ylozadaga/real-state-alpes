from __future__ import annotations
from dataclasses import dataclass, field

import src.company_data_collector.modules.company.domain.value_objects as ov
from src.company_data_collector.modules.company.domain.events import CompanyCreated


@dataclass
class Company(ov):
    id_cliente: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoReserva = field(default=ov.EstadoReserva.PENDIENTE)
    itinerarios: list[ov.Itinerario] = field(default_factory=list[ov.Itinerario])

    def create_company(self, company: Company):
        self.id: str = field(default_factory=str)
        self.registration_date: str = field(default_factory=str)
        self.renovation_date: str = field(default_factory=str)
        self.nit: str = field(default_factory=str)
        self.acronym: str = field(default_factory=str)
        self.status: str = field(default_factory=str)
        self.validity: str = field(default_factory=str)
        self.organization_type: str = field(default_factory=str)
        self.registration_category: str = field(default_factory=str)


        self.agregar_evento(CompanyCreated(id_reserva=self.id, id_cliente=self.id_cliente, estado=self.estado.name,
                                          fecha_creacion=self.fecha_creacion))
