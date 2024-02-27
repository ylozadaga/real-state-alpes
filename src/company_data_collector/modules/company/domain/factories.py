from .entities import Company
from .rules import MinimoUnItinerario
from .exceptions import ObjectTypeNotExistInDomainCompanyException
from src.company_data_collector.seedwork.domain.repositories import Mapper, Repository
from src.company_data_collector.seedwork.domain.factories import Factory
from src.company_data_collector.seedwork.domain.entities import Entity
from dataclasses import dataclass


@dataclass
class CompanyFactory(Factory):

    def create_objet(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            company: Company = mapper.dto_to_entity(obj)

            self.validate_rule(MinimoUnItinerario(reserva.itinerarios))

            return company
