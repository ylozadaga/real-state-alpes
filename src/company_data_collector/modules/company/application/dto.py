from dataclasses import dataclass
from ....seedwork.application.dto import DTO


@dataclass(frozen=True)
class CompanyDTO(DTO):
    company_id: str
    nit: str
    acronym: str
    status: str
    validity: str
    organization_type: str
    registration_category: str
