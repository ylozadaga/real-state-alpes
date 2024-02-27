from src.company_data_collector.seedwork.application.commands import Command
from src.company_data_collector.modules.company.application.dto import CompanyDTO
from .base import CreateCompanyBaseHandler
from dataclasses import dataclass, field
from src.company_data_collector.seedwork.application.commands import execute_command as command

from src.company_data_collector.modules.company.domain.entities import Company
from src.company_data_collector.seedwork.infrastructure.uow import UnitWorkPort
from src.company_data_collector.modules.company.application.mappers import CompanyMapper
from src.company_data_collector.modules.company.intrastructure.repositories import CompanyRepository


@dataclass
class CreateCompany(Command):
    id: str
    registration_date: str
    renovation_date: str
    nit: str
    acronym: str
    status: str
    validity: str
    organization_type: str
    registration_category: str


class CreateCompanyHandler(CreateCompanyBaseHandler):

    def handle(self, command_create_company: CreateCompany):
        company_dto = CompanyDTO(
            id=command_create_company.id,
            registration_date=command_create_company.registration_date,
            renovation_date=command_create_company.renovation_date,
            nit=command_create_company.nit,
            acronym=command_create_company.acronym,
            status=command_create_company.status,
            validity=command_create_company.validity,
            organization_type=command_create_company.organization_type,
            registration_category=command_create_company.registration_category)

        company: Company = self.company_factory.create_object(company_dto, CompanyMapper())
        company.create_company(company)

        repository = self.repository_factory.create_object(CompanyRepository.__class__)

        UnitWorkPort.register_batch(repository.agregar, company)
        UnitWorkPort.savepoint()
        UnitWorkPort.commit()


@command.register(CreateCompany)
def execute_command_create_company(command_create_company: CreateCompany):
    handler = CreateCompanyHandler()
    handler.handle(command_create_company)
