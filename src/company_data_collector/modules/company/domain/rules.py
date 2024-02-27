from src.company_data_collector.seedwork.domain.rules import BusinessRule
from .value_objects import Ruta
from .entities import Pasajero


class MinimoUnAdulto(BusinessRule):

    pasajeros: list[Pasajero]

    def __init__(self, pasajeros, mensaje='Al menos un adulto debe ser parte del itinerario'):
        super().__init__(mensaje)
        self.pasajeros = pasajeros

    def es_valido(self) -> bool:
        for pasajero in self.pasajeros:
            if pasajero.tipo == TipoPasajero.ADULTO:
                return True
        return False
