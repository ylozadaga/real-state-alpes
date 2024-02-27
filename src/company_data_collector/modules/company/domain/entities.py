from __future__ import annotations
from dataclasses import dataclass, field

import aeroalpes.modulos.vuelos.dominio.objetos_valor as ov
from aeroalpes.modulos.vuelos.dominio.eventos import ReservaCreada, ReservaAprobada, ReservaCancelada, ReservaPagada
from aeroalpes.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad


@dataclass
class Company(AgregacionRaiz):
    id_cliente: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoReserva = field(default=ov.EstadoReserva.PENDIENTE)
    itinerarios: list[ov.Itinerario] = field(default_factory=list[ov.Itinerario])

    def create_company(self, reserva: Company):
        self.id_cliente = reserva.id_cliente
        self.estado = reserva.estado
        self.itinerarios = reserva.itinerarios

        self.agregar_evento(ReservaCreada(id_reserva=self.id, id_cliente=self.id_cliente, estado=self.estado.name,
                                          fecha_creacion=self.fecha_creacion))
