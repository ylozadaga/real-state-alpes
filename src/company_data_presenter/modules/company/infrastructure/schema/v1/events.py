from pulsar.schema import *
from src.company_data_collector.seedwork.infrastructure.schema.v1.events import IntegrationEvent


class CompanyCreatedPayload(Record):
    id_company = String()
    status = String()
    creation_date = Long()


class EventCompanyCreated(IntegrationEvent):
    data = CompanyCreatedPayload()

