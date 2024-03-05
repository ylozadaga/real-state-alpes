from .entities import Company
from .rules import IsValidDataFormat
from .exceptions import ObjectTypeNotExistInDomainCompanyException
from ....seedwork.domain.repositories import Mapper, Repository
from ....seedwork.domain.factories import Factory
from ....seedwork.domain.entities import Entity
from dataclasses import dataclass


@dataclass
class CompanyFactory(Factory):

    def create_object(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            company: Company = mapper.dto_to_entity(obj)
            return company
