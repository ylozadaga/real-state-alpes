from pulsar.schema import *
from ......seedwork.infrastructure.schema.v1.commands import (IntegrationCommand)


class CreateCompanyPayloadCommand(IntegrationCommand):
    company_id = String()
    nit = String()
    acronym = String()
    status = String()
    validity = String()
    organization_type = String()
    registration_category = String()


class CreateCompanyCommand(IntegrationCommand):
    data = CreateCompanyPayloadCommand()
