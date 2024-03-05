from .....seedwork.application.commands import Command
from ...application.dto import CompanyDTO
from .base import CreateCompanyBaseHandler
from dataclasses import dataclass
from ...infrastructure.schema.v1.commands import CreateCompanyPayloadCommand
from .....seedwork.application.commands import execute_command as command

from .....modules.company.domain.entities import Company
from .....seedwork.infrastructure.uow import UnitWorkPort
from ....company.application.mappers import CompanyMapper
from ....company.infrastructure.repositories import CompanyRepository


@dataclass
class CreateCompany(Command):
    company_id: str
    nit: str
    acronym: str
    status: str
    validity: str
    organization_type: str
    registration_category: str

    def __init__(self, company_data: CreateCompanyPayloadCommand | CompanyDTO):
        self.company_id = company_data.company_id
        self.nit = company_data.nit
        self.acronym = company_data.acronym
        self.status = company_data.status
        self.validity = company_data.validity
        self.organization_type = company_data.organization_type
        self.registration_category = company_data.registration_category


class CreateCompanyHandler(CreateCompanyBaseHandler):

    def handle(self, command_create_company: CreateCompany):
        company_dto = CompanyDTO(
            company_id=command_create_company.company_id,
            nit=command_create_company.nit,
            acronym=command_create_company.acronym,
            status=command_create_company.status,
            validity=command_create_company.validity,
            organization_type=command_create_company.organization_type,
            registration_category=command_create_company.registration_category)

        company: Company = self.company_factory.create_object(company_dto, CompanyMapper())
        company.create_company()

        repository = self.repository_factory.create_object(CompanyRepository.__class__)

        UnitWorkPort.register_batch(repository.add, company)
        UnitWorkPort.savepoint()
        UnitWorkPort.commit()


@command.register(CreateCompany)
def execute_command_create_company(command_create_company: CreateCompany):
    handler = CreateCompanyHandler()
    handler.handle(command_create_company)
