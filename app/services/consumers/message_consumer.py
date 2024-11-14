import os

from app.services.kafka_tools.consumer import consume
from app.services.producers.explosive_producer import produce_explosive_message
from app.services.producers.hostage_producer import produce_hostage_message


def consume_message():

    def analyze_threat(message):
        sentences = message['sentences']
        for s in sentences:
            sen = s.strip(".,?!").lower()
            if "explosive" in sen:
                produce_explosive_message(message)
                return
            if "hostage" in sen:
                produce_hostage_message(message)
                return

    consume(
        topic_name=os.environ['TOPIC_ALL_MESSAGES_NAME'],
        func=analyze_threat
    )

if __name__ == '__main__':
    consume_message()