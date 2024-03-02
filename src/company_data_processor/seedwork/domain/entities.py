from dataclasses import dataclass, field
from .events import DomainEvent
from .mixins import ValidateRulesMixin
from .rules import IdEntityIsImmutable
from .exceptions import IdMustBeImmutableException
from datetime import datetime
import uuid


@dataclass
class Entity:
    id: uuid.UUID = field(hash=True)
    _id: uuid.UUID = field(init=False, repr=False, hash=True)
    source: str = field(default=None)
    creation_date: datetime = field(default=datetime.now())
    update_date: datetime = field(default=datetime.now())

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


@dataclass
class RootAggregation(Entity, ValidateRulesMixin):
    events: list[DomainEvent] = field(default_factory=list)

    def add_event(self, event: DomainEvent):
        self.events.append(event)

    def clear_events(self):
        self.events = list()
