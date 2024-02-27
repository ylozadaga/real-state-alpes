from src.company_data_collector.seedwork.application.services import Service
from src.company_data_collector.modules.company.domain.entities import Company
from src.company_data_collector.modules.company.domain.factories import CompanyFactory
from src.company_data_collector.modules.company.intrastructure.factories import RepositoryFactory
from src.company_data_collector.modules.company.intrastructure.repositories import CompanyRepository
from src.company_data_collector.seedwork.infrastructure.uow import UnitWorkPort
from .mappers import CompanyMapper
from .dto import CompanyDTO


class CompanyService(Service):

    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._company_factory: CompanyFactory = CompanyFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def company_factory(self):
        return self._company_factory

    def create_company(self, company_dto: CompanyDTO) -> CompanyDTO:
        company: Company = self.company_factory.create_object(company_dto, CompanyMapper)
        company.crear_reserva(company)

        repository = self.repository_factory.create_object(CompanyRepository.__class__)

        UnitWorkPort.register_batch(repository.add, company)
        UnitWorkPort.savepoint()
        UnitWorkPort.commit()

        return self.company_factory.create_object(company, CompanyMapper)
