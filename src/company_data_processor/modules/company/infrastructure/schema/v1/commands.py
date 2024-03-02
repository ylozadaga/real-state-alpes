from pulsar.schema import *
from company_data_processor.seedwork.infrastructure.schema.v1.commands import (IntegrationCommand)


class CommandCreateCompanyPayload(IntegrationCommand):
    id_company = String()


class CommandCreateCompany(IntegrationCommand):
    data = CommandCreateCompanyPayload()
