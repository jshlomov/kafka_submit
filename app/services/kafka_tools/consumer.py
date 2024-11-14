import json
import os

from dotenv import load_dotenv
from kafka import KafkaConsumer

load_dotenv(verbose=True)

def consume_message(topic_name:str, func = lambda x: x, mode ='latest'):
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer= lambda value: json.loads(value.decode('utf-8')),
        auto_offset_reset=mode
    )

    for message in consumer:
        func(message.value)
        print(f"Recieved: {message.key}: {message.value}")