from dataclasses import dataclass
from abc import ABC
from datetime import datetime


@dataclass(frozen=True)
class ValueObject:
    ...


@dataclass(frozen=True)
class Code(ABC, ValueObject):
    code: str


@dataclass(frozen=True)
class Country(ValueObject):
    code: Code
    name: str


@dataclass(frozen=True)
class City(ValueObject):
    country: Country
    code: Code
    name: str
