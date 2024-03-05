from dataclasses import dataclass
from company_data_presenter.seedwork.application.queries import Query, QueryHandler, QueryResult
from company_data_presenter.seedwork.application.queries import execute_query as query
from company_data_presenter.modules.company.infrastructure.repositories import CompanyRepository
from .base import CompanyQueryBaseHandler
from company_data_presenter.modules.company.application.mappers import CompanyMapper
import uuid


@dataclass
class GetCompany(Query):
    id: str

class GetCompanyHandler(CompanyQueryBaseHandler):
    def handle(self, query: GetCompany) -> QueryResult:
        repository = self.company_repository.create_object(CompanyRepository.__class__)
        company = self.company_factory.create_object(repository.get_by_id(query.id), CompanyMapper())
        return QueryResult(result=company)

@query.register(GetCompany)
def execute_query_get_company(query: GetCompany):
    handler = GetCompanyHandler()
    return handler.handle(query)

