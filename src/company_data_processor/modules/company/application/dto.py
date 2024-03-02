from dataclasses import dataclass, field
from src.company_data_processor.seedwork.application.dto import DTO


@dataclass(frozen=True)
class CompanyDTO(DTO):
    id: str = field(default_factory=str)
    registration_date: str = field(default_factory=str)
    renovation_date: str = field(default_factory=str)
    nit: str = field(default_factory=str)
    acronym: str = field(default_factory=str)
    status: str = field(default_factory=str)
    validity: str = field(default_factory=str)
    organization_type: str = field(default_factory=str)
    registration_category: str = field(default_factory=str)
