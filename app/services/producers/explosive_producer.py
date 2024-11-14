import os

from dotenv import load_dotenv

from app.services.kafka_tools.producer import produce

load_dotenv(verbose=True)

def produce_explosive_message(message):
    produce(
        topic_name=os.environ['TOPIC_MESSAGES_EXPLOSIVE_NAME'],
        message=message,
        key=message['email']
    )