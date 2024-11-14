import os

from app.repository.mongo_repository import insert_message
from app.services.kafka_tools.consumer import consume


def consume_to_mongo():
    consume(
        topic_name=os.environ['TOPIC_ALL_MESSAGES_NAME'],
        func=insert_message
    )

if __name__ == '__main__':
    consume_to_mongo()