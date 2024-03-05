from dataclasses import dataclass, field
from ....seedwork.domain.factories import Factory
from ....seedwork.domain.repositories import Repository
from ....modules.company.domain.repositories import CompanyRepository
from .repositories import CompanyRepositorySQLite
from .exceptions import FactoryException


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == CompanyRepository.__class__:
            return CompanyRepositorySQLite()
        else:
            raise FactoryException()
