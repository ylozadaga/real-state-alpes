from ....config.db import db
from ..domain.repositories import CompanyRepository
from ..domain.entities import Company
from ..domain.factories import CompanyFactory
from .dto import Company as CompanyDTO
from .mappers import CompanyMapper
from uuid import UUID


class CompanySQLiteRepository(CompanyRepository):

    def __init__(self):
        self._company_factory: CompanyFactory = CompanyFactory()

    @property
    def company_factory(self):
        return self._company_factory

    def get_by_id(self, id: UUID) -> Company:
        company_dto = db.session.query(CompanyDTO).filter_by(id=str(id)).one()
        return self.company_factory.create_object(company_dto, CompanyMapper())

    def get_all(self) -> list[Company]:
        raise NotImplementedError

    def add(self, company: Company):
        company_dto = self.company_factory.create_object(company, CompanyMapper())
        db.session.add(company_dto)
        db.session.commit()
        db.session.refresh(company_dto)

    def update(self, company: Company):
        raise NotImplementedError

    def delete(self, company_id: UUID):
        raise NotImplementedError
