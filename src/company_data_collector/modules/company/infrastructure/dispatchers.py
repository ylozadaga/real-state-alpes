import pulsar
from pulsar.schema import *
from .schema.v1.events import CompanyCreatedEvent, CompanyCreatedPayload
from .schema.v1.commands import CreateCompanyCommand, CreateCompanyPayloadCommand
from ....seedwork.infrastructure import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Dispatcher:

    def _publish_message(self, message, topic, data_schema):
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        producer = client.create_producer(topic, schema=data_schema)
        producer.send(message)
        client.close()

    def publish_event(self, event, topic):
        payload = CompanyCreatedPayload(
            id_company=event.id_company,
            status=event.status,
            creation_date=unix_time_millis(event.creation_date)
        )
        integration_event = CompanyCreatedEvent(data=payload)
        self._publish_message(integration_event, topic, AvroSchema(CompanyCreatedEvent))

    def publish_command(self, command, topic):
        payload = CreateCompanyPayloadCommand(
            company_id=str(command.company_id),
            acronym=str(command.acronym),
            nit=str(command.nit),
            status=str(command.status),
            validity=str(command.validity),
            organization_type=str(command.organization_type),
            registration_category=str(command.registration_category)
        )
        integration_command = CreateCompanyCommand(data=payload)
        self._publish_message(integration_command, topic, AvroSchema(CreateCompanyCommand))
