import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from src.company_data_collector.modules.company.infrastructure.schema.v1.events import EventCompanyCreated
from src.company_data_collector.modules.company.infrastructure.schema.v1.commands import CommandCreateCompany
from src.company_data_collector.seedwork.infrastructure import utils


def subscribe_to_events():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('events-company',
                                    consumer_type=_pulsar.ConsumerType.Shared,
                                    subscription_name='rs-alpes-sub-events',
                                    schema=AvroSchema(EventCompanyCreated))

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
                                    schema=AvroSchema(CommandCreateCompany))

        while True:
            message = consumer.receive()
            print(f'Command receive: {message.value().data}')

            consumer.acknowledge(message)

        client.close()
    except:
        logging.error('ERROR: Subscribing to command topic!')
        traceback.print_exc()
        if client:
            client.close()
