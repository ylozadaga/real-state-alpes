from abc import ABC, abstractmethod
from .repositories import Mapper
from .mixins import ValidateRulesMixin


class Factory(ABC, ValidateRulesMixin):
    @abstractmethod
    def create_object(self, obj: any, mapper: Mapper = None) -> any:
        ...
