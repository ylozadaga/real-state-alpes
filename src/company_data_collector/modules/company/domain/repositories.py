from abc import ABC
from company_data_collector.seedwork.domain.repositories import Repository


class CompanyRepository(Repository, ABC):
    ...
