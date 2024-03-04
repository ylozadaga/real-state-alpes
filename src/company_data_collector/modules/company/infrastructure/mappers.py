from .dto import Company as CompanyDTO
from ..domain.entities import Company
from ....seedwork.domain.repositories import Mapper


class CompanyMapper(Mapper):

    def get_type(self) -> type:
        return Company.__class__

    def entity_to_dto(self, entity: Company) -> CompanyDTO:
        company_dto = CompanyDTO()
        company_dto.id = str(entity.id)
        company_dto.nit = entity.nit
        company_dto.acronym = entity.acronym
        company_dto.status = entity.status
        company_dto.validity = entity.validity
        company_dto.organization_type = entity.organization_type
        company_dto.registration_category = entity.registration_category
        return company_dto

    def dto_to_entity(self, company_dto: CompanyDTO) -> Company:
        return Company(company_dto)
