import pulsar
from pulsar.schema import *

from . import utils

class Dispatcher:
    def __init__(self):
        ...
    
    async def publish_message(self, message, topic, schema):
        json_schema = utils.get_schema_registry(schema)
        avro_schema = utils.get_schema_avro_from_dict(json_schema)

        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')#TODO revisar puerto
        producer = client.create_producer(topic, schema=avro_schema)
        producer.send(message)
        client.close()