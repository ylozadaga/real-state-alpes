from abc import ABC
from src.company_data_presenter.seedwork.domain.repositories import Repository


class CompanyRepository(Repository, ABC):
    ...
