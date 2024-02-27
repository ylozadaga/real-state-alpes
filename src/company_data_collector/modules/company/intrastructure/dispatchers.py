import pulsar
from pulsar.schema import *
from src.company_data_collector.modules.company.intrastructure.schema.v1.events import (EventCompanyCreated,
                                                                                        CompanyCreatedPayload)
from src.company_data_collector.modules.company.intrastructure.schema.v1.commands import (CommandCreateCompany,
                                                                                          CommandCreateCompanyPayload)
from src.company_data_collector.seedwork.infrastructure import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Dispatcher:

    def _publish_message(self, message, topic, schema):
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publisher = client.create_producer(topic, schema=AvroSchema(EventCompanyCreated))
        publisher.send(message)
        client.close()

    def publish_event(self, event, topic):
        payload = CompanyCreatedPayload(
            id_company=str(event.id_reserva),
            estado=str(event.estado),
            creation_date=int(unix_time_millis(event.creation_date))
        )
        integration_event = EventCompanyCreated(data=payload)
        self._publish_message(integration_event, topic, AvroSchema(EventCompanyCreated))

    def publish_command(self, command, topic):
        payload = CommandCreateCompanyPayload(
            id_company=str(command.id_company)
        )
        integration_command = CommandCreateCompany(data=payload)
        self._publish_message(integration_command, topic, AvroSchema(CommandCreateCompany))
