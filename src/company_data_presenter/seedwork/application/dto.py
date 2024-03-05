from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(frozen=True)
class DTO:
    ...


class Mapper(ABC):

    @abstractmethod
    def outer_to_dto(self, outer: any) -> DTO:
        ...

    @abstractmethod
    def dto_to_outer(self, dto: DTO) -> any:
        ...
