import logging
import traceback
import pulsar, _pulsar
import aiopulsar
import asyncio
from pulsar.schema import *
from . import utils

async def subscribe_to_topic(topic: str, subscription: str, schema: str, consumer_type: _pulsar.ConsumerType.Shared, events=[]):
    try:
        json_schema = utils.get_schema_registry(schema)
        avro_schema = utils.get_schema_avro_from_dict(json_schema)
        async with aiopulsar.connect(f'pulsar://{utils.broker_host()}:6650') as client:
            async with client.subscribe(
                topic,
                consumer_type=consumer_type,
                subscription_name=subscription,
                schema=avro_schema
            ) as consumer:
                while True:
                    message=await consumer.receive()
                    print(message)
                    data=message.value()
                    print(f'Event received: {data}')
                    events.append(str(data))
                    await consumer.acknowledge(message)
    
    except:
        logging.error(f'ERROR: Subscribing to events topic! {topic}, {subscription}, {schema}')
        traceback.print_exc()