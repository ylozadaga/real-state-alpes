from company_data_collector.seedwork.application.commands import CommandHandler
from company_data_collector.modules.company.infrastructure.factories import RepositoryFactory
from company_data_collector.modules.company.domain.factories import CompanyFactory


class CreateCompanyBaseHandler(CommandHandler):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._company_factory: CompanyFactory = CompanyFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def company_factory(self):
        return self._company_factory
