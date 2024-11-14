import os

from dotenv import load_dotenv

from app.services.kafka_tools.producer import produce

load_dotenv(verbose=True)

def produce_message(message):
    produce(
        topic_name=os.environ['TOPIC_ALL_MESSAGES_NAME'],
        message=message,
        key=message['email']
    )