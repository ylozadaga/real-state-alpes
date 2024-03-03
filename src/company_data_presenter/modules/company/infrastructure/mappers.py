from company_data_presenter.seedwork.domain.repositories import Mapper
from company_data_presenter.modules.company.domain.entities import Company
from .dto import Company as CompanyDTO


class CompanyMapper(Mapper):
    _DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

    def get_type(self) -> type:
        return Company.__class__

    def entity_to_dto(self, entity: Company) -> CompanyDTO:
        company_dto = CompanyDTO()
        company_dto.id = str(entity.id)
        company_dto.registration_date = entity.registration_date
        company_dto.renovation_date = entity.renovation_date
        company_dto.nit = entity.nit
        company_dto.acronym = entity.acronym
        company_dto.status = entity.status
        company_dto.validity = entity.validity
        company_dto.organization_type = entity.organization_type
        company_dto.registration_category = entity.registration_category
        return company_dto

    def dto_to_entity(self, company_dto: CompanyDTO) -> Company:
        company = Company(
            company_dto.id,
            company_dto.registration_date,
            company_dto.renovation_date,
            company_dto.nit,
            company_dto.acronym,
            company_dto.status,
            company_dto.validity,
            company_dto.organization_type,
            company_dto.registration_category,
        )
        return company