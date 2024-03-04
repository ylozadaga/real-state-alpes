from ....seedwork.application.services import Service
from ..domain.entities import Company
from ..domain.factories import CompanyFactory
from ..infrastructure.factories import RepositoryFactory
from ..infrastructure.repositories import CompanyRepository
from ....seedwork.infrastructure.uow import UnitWorkPort
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
        company: Company = self.company_factory.create_object(company_dto, CompanyMapper())

        repository = self.repository_factory.create_object(CompanyRepository.__class__)

        UnitWorkPort.register_batch(repository.add, company)
        UnitWorkPort.savepoint()
        UnitWorkPort.commit()

        return self.company_factory.create_object(company, CompanyMapper())
