from ....seedwork.application.dto import Mapper as AppMapper
from ....seedwork.domain.repositories import Mapper as RepositoryMapper
from ....modules.company.domain.entities import Company
from .dto import CompanyDTO


class MapperCompanyDTOJson(AppMapper):

    def outer_to_dto(self, outer: dict) -> CompanyDTO:
        company_dto = CompanyDTO(**outer)
        return company_dto

    def dto_to_outer(self, dto: CompanyDTO) -> dict:
        return dto.__dict__


class CompanyMapper(RepositoryMapper):

    def get_type(self) -> type:
        return Company.__class__

    def entity_to_dto(self, entity: Company) -> CompanyDTO:
        return CompanyDTO(
            nit=entity.nit,
            acronym=entity.acronym,
            status=entity.status,
            validity=entity.validity,
            organization_type=entity.organization_type,
            registration_category=entity.registration_category
        )

    def dto_to_entity(self, dto: CompanyDTO) -> Company:
        return Company(
            nit=dto.nit,
            acronym=dto.acronym,
            status=dto.status,
            validity=dto.validity,
            organization_type=dto.organization_type,
            registration_category=dto.registration_category
        )

