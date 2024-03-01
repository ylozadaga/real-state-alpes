from dataclasses import dataclass, field
from .rules import IdEntityIsImmutable
from .exceptions import IdMustBeImmutableException
from datetime import datetime
import uuid


@dataclass
class DomainEvent:
    id: uuid.UUID = field(hash=True)
    _id: uuid.UUID = field(init=False, repr=False, hash=True)
    event_date: datetime = field(default=datetime.now())

    @classmethod
    def next_id(self) -> uuid.UUID:
        return uuid.uuid4()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: uuid.UUID) -> None:
        if not IdEntityIsImmutable(self).is_valid():
            raise IdMustBeImmutableException()
        self._id = self.next_id()
