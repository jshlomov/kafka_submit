import os

from dotenv import load_dotenv
from app.services.kafka_tools.consumer import consume

load_dotenv(verbose=True)

def consume_hostage():
    consume(
        topic_name=os.environ['TOPIC_MESSAGES_HOSTAGE_NAME']
    )

if __name__ == '__main__':
    consume_hostage()