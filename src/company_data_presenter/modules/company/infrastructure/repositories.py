from company_data_presenter.config.db import db
from company_data_presenter.modules.company.domain.repositories import CompanyRepository
from company_data_presenter.modules.company.domain.entities import Company
from company_data_presenter.modules.company.domain.factories import CompanyFactory
from .dto import Company as CompanyDTO
from .mappers import CompanyMapper
from uuid import UUID


class CompanyRepositorySQLite(CompanyRepository):

    def __init__(self):
        self._company_factory: CompanyFactory = CompanyFactory()

    @property
    def company_factory(self):
        return self._company_factory

    def get_by_id(self, id: UUID) -> Company:
        company_dto = db.session.query(CompanyDTO).filter_by(id=str(id)).one()
        return self.company_factory.create_object(company_dto, CompanyMapper())

    def get_all(self) -> list[Company]:
        companies = db.session.query(CompanyDTO).all()     
        return [company for company in companies (self.company_factory.create_object(company, CompanyMapper()))] 
