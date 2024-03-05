from ....seedwork.application.services import Service
from ....modules.company.domain.entities import Company
from ....modules.company.domain.factories import CompanyFactory
from ....modules.company.infrastructure.factories import RepositoryFactory
from ....modules.company.infrastructure.repositories import CompanyRepository
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

    def find_company_by_id(self, id) -> CompanyDTO:
        repository = self.repository_factory.create_object(CompanyRepository.__class__)
        return repository.get_by_id(id).__dict__

    
    def find_all_companies(self) -> list[CompanyDTO]:
        repository = self.repository_factory.create_object(CompanyRepository.__class__)
        return repository.get_all().__dict__

