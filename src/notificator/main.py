import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import os


def time_millis():
    return int(time.time() * 1000)


class IntegrationEvent(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    spec_version = String()
    type = String()
    data_content_type = String()
    service_name = String()


class CompanyDataCollectedPayload(Record):
    id_company = String()
    status = String()
    creation_date = Long()


class CompanyDataCollectedEvent(IntegrationEvent):
    data = CompanyDataCollectedPayload()


HOSTNAME = os.getenv('PULSAR_ADDRESS', default="localhost")

client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')
consumer = client.subscribe('events-company',
                            consumer_type=_pulsar.ConsumerType.Shared,
                            subscription_name='sub-notificator-events-company-collector',
                            schema=AvroSchema(CompanyDataCollectedEvent))

while True:
    msg = consumer.receive()
    print('=========================================')
    print("Message Receive:  '%s'" % msg.value().data)
    print('=========================================')
    consumer.acknowledge(msg)

client.close()
