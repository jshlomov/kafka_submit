from returns.result import Success
from toolz import curry

from app.db.models import PersonMessage, Location, DeviceInfo, SuspiciousExplosiveContent, SuspiciousHostageContent
from app.repository.postgres_repository.Location_repository import insert_location
from app.repository.postgres_repository.device_info_repository import insert_device_info
from app.repository.postgres_repository.person_repository import insert_person
from app.repository.postgres_repository.suspicious_explosive_repository import insert_explosive_content
from app.repository.postgres_repository.suspicious_hostage_repository import insert_hostage_content



def convert_json_to_person(message):
    return PersonMessage(
        email=message["email"],
        username=message["username"],
        ip_address=message["ip_address"],
        created_at=message["created_at"]
    )

def convert_json_to_location(message, person_id):
    return Location(
        latitude=message["location"]["latitude"],
        longitude=message["location"]["longitude"],
        city=message["location"]["city"],
        country=message["location"]["country"],
        person_id=person_id
    )

def convert_json_to_device_info(message, person_id):
    return DeviceInfo(
        browser=message["device_info"]["browser"],
        os=message["device_info"]["os"],
        device_id=message["device_info"]["device_id"],
        person_id=person_id
    )

def convert_json_to_explosive_contents(message, person_id):
    return [
        SuspiciousExplosiveContent(
            sentence=sen,
            person_id=person_id
        )
        for sen in message['sentences']
    ]

def convert_json_to_hostage_contents(message, person_id):
    hostage_content_list = [
        SuspiciousHostageContent(
            sentence=sen,
            person_id=person_id
        )
        for sen in message['sentences']
    ]
    sorted_hostage_content = sorted(
        hostage_content_list,
        key=lambda x: 'hostage' in x.sentence.lower(),
        reverse=True
    )
    return sorted_hostage_content

@curry
def insert_all_message(message, convert_sentences_func, insert_sentences_func):

    person_message = convert_json_to_person(message)

    person_id :int
    result = insert_person(person_message)
    if isinstance(result, Success):
        person_id = result.unwrap().id
    else:
        print(f"Failed to insert person: {result.unwrap()}")
        return

    location = convert_json_to_location(message, person_id)
    insert_location(location)

    device_info = convert_json_to_device_info(message, person_id)
    insert_device_info(device_info)

    sentences = convert_sentences_func(message, person_id)
    for sen in sentences:
        insert_sentences_func(sen)