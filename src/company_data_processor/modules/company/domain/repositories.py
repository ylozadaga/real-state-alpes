from abc import ABC
from company_data_processor.seedwork.domain.repositories import Repository


class CompanyRepository(Repository, ABC):
    ...
