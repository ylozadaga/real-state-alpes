import pulsar, _pulsar
from pulsar.schema import *
from flask.ctx import AppContext, RequestContext
import logging
import traceback

from ....modules.company.infrastructure.schema.v1.events import CompanyCreatedEvent
from ....modules.company.infrastructure.schema.v1.commands import CreateCompanyCommand
from ....seedwork.infrastructure import utils
from ....seedwork.application.commands import execute_command


def subscribe_to_events():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('events-company',
                                    consumer_type=_pulsar.ConsumerType.Shared,
                                    subscription_name='rs-alpes-sub-events',
                                    schema=AvroSchema(CompanyCreatedEvent))

        while True:
            message = consumer.receive()
            print(f'Event receive: {message.value().data}')

            consumer.acknowledge(message)

        client.close()
    except:
        logging.error('ERROR: Subscribing to events topic!')
        traceback.print_exc()
        if client:
            client.close()


def subscribe_to_commands():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('commands-company',
                                    consumer_type=_pulsar.ConsumerType.Shared,
                                    subscription_name='rs-alpes-sub-commands',
                                    schema=AvroSchema(CreateCompanyCommand))

        while True:
            message = consumer.receive()
            print(f'Command receive: {message.value().data}')

            data = message.value().data
            command = CreateCompanyCommand(data)
            ##with context and req_context:
            execute_command(command)
            consumer.acknowledge(message)

        client.close()
    except Exception:
        logging.error('ERROR: Subscribing to command topic!')
        traceback.print_exc()
        if client:
            client.close()
