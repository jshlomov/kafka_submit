import os

from dotenv import load_dotenv

from app.repository.postgres_repository.suspicious_hostage_repository import insert_hostage_content
from app.services.kafka_tools.consumer import consume
from app.services.make_email_service import insert_all_message, convert_json_to_explosive_contents

load_dotenv(verbose=True)

def consume_explosive():
    consume(
        topic_name=os.environ['TOPIC_MESSAGES_EXPLOSIVE_NAME'],
        func=insert_all_message(
            convert_sentences_func=convert_json_to_explosive_contents,
            insert_sentences_func=insert_hostage_content
        )
    )

if __name__ == '__main__':
    consume_explosive()