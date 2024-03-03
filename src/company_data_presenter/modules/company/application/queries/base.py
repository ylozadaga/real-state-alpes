from company_data_presenter.seedwork.application.queries import QueryHandler
from company_data_presenter.modules.company.infrastructure.factories import CompanyRepository
from company_data_presenter.modules.company.domain.factories import CompanyFactory


class CompanyQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._company_repository: CompanyRepository = CompanyRepository()
        self._company_factory: CompanyFactory = CompanyFactory()

    @property
    def company_repository(self):
        return self._company_repository

    @property
    def company_factory(self):
        return self._company_factory
