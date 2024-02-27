from src.company_data_collector.config.db import db
from src.company_data_collector.modules.company.domain.repositories import CompanyRepository
from aeroalpes.modulos.vuelos.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from aeroalpes.modulos.vuelos.dominio.entidades import Proveedor, Aeropuerto, Reserva
from aeroalpes.modulos.vuelos.dominio.fabricas import FabricaVuelos
from .dto import Company as CompanyDTO
from .mappers import MapeadorReserva
from uuid import UUID


class CompanyRepositorySQLite(RepositorioReservas):

    def __init__(self):
        self._fabrica_vuelos: FabricaVuelos = FabricaVuelos()

    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos

    def obtener_por_id(self, id: UUID) -> Reserva:
        reserva_dto = db.session.query(ReservaDTO).filter_by(id=str(id)).one()
        return self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())

    def obtener_todos(self) -> list[Reserva]:
        # TODO
        raise NotImplementedError

    def agregar(self, reserva: Reserva):
        reserva_dto = self.fabrica_vuelos.crear_objeto(reserva, MapeadorReserva())
        db.session.add(reserva_dto)

    def actualizar(self, reserva: Reserva):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError
