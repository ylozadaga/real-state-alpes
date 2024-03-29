from .entities import Company
from .rules import IsValidDataFormat
from .exceptions import ObjectTypeNotExistInDomainCompanyException
from company_data_processor.seedwork.domain.repositories import Mapper, Repository
from company_data_processor.seedwork.domain.factories import Factory
from company_data_processor.seedwork.domain.entities import Entity
from dataclasses import dataclass


@dataclass
class CompanyFactory(Factory):

    def create_objet(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            company: Company = mapper.dto_to_entity(obj)

            validate_rule(IsValidDataFormat(company))

            return company
