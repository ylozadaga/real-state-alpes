from pulsar.schema import *
from ......seedwork.infrastructure.schema.v1.events import IntegrationEvent


class CompanyCreatedPayload(Record):
    id_company = String()
    status = String()
    creation_date = String()


class CompanyCreatedEvent(IntegrationEvent):
    data = CompanyCreatedPayload()
