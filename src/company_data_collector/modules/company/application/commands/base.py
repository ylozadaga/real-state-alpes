from company_data_collector.seedwork.application.commands import CommandHandler
from src.company_data_collector.modulos.company.infrastructure.factories import FactoryRepository, FactoryCompany
from aeroalpes.modulos.vuelos.infraestructura.fabricas import FabricaRepositorio
from aeroalpes.modulos.vuelos.dominio.fabricas import FabricaVuelos


class CreateCompanyBaseHandler(CommandHandler):
    def __init__(self):
        self._factory_repository: FactoryRepository = FactoryRepository()
        self._factory_company: FactoryCompany = FactoryCompany()

    @property
    def factory_repository(self):
        return self._factory_repository

    @property
    def factory_company(self):
        return self._factory_company