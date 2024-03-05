from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass, field

from company_data_presenter.seedwork.domain.entities import RootAggregation
from company_data_presenter.modules.company.domain.events import CompanyCreated


@dataclass
class Company(RootAggregation):
    id: str = None
    registration_date: datetime = None
    renovation_date: datetime = None
    nit: str = None
    acronym: str = None
    status: str = None
    validity: str = None
    organization_type: str = None
    registration_category: str = None

    def create_company(self, company: Company):
        self.id = company.id
        self.registration_date = company.registration_date
        self.renovation_date = company.renovation_date
        self.nit = company.nit
        self.acronym = company.acronym
        self.status = company.status
        self.validity = company.validity
        self.organization_type = company.organization_type
        self.registration_category = company.registration_category

        self.add_event(CompanyCreated(
            id=self.id,
            registration_date=self.registration_date,
            renovation_date=self.renovation_date,
            nit=self.nit,
            acronym=self.acronym,
            status=self.status,
            validity=self.validity,
            organization_type=self.organization_type,
            registration_category=self.registration_category))
