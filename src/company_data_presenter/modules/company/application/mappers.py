from ....seedwork.application.dto import Mapper as AppMap
from ....seedwork.domain.repositories import Mapper as RepMap
from ....modules.company.domain.entities import Company
from .dto import CompanyDTO


class MapperCompanyDTOJson(AppMap):

    def outer_to_dto(self, outer: dict) -> CompanyDTO:
        company_dto = CompanyDTO()
        return company_dto

    def dto_to_outer(self, dto: CompanyDTO) -> dict:
        return dto.__dict__


class CompanyMapper(RepMap):
    DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

    def get_type(self) -> type:
        return Company.__class__

    def entity_to_dto(self, entity: Company) -> CompanyDTO:
        creation_date = entity.creation_date.strftime(self.DATE_FORMAT)
        update_date = entity.update_date.strftime(self.DATE_FORMAT)
        _id = str(entity.id)
        return CompanyDTO(creation_date, update_date, _id)

    def dto_to_entity(self, dto: CompanyDTO) -> Company:
        company = Company()
        return company
