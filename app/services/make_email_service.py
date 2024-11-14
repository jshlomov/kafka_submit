from returns.result import Success

from app.db.models import PersonMessage, Location, DeviceInfo, SuspiciousExplosiveContent, SuspiciousHostageContent
from app.repository.postgres_repository.Location_repository import insert_location
from app.repository.postgres_repository.device_info_repository import insert_device_info
from app.repository.postgres_repository.person_repository import insert_person
from app.repository.postgres_repository.suspicious_explosive_repository import insert_explosive_content
from app.repository.postgres_repository.suspicious_hostage_repository import insert_hostage_content


def convert_message(message, destiny):

    person_message = PersonMessage(
        email=message["email"],
        username=message["username"],
        ip_address=message["ip_address"],
        created_at=message["created_at"]
    )

    person_id :int
    result = insert_person(person_message)
    if isinstance(result, Success):
        person_id = result.unwrap().id
    else:
        print(f"Failed to insert person: {result.unwrap()}")
        return

    location = Location(
        latitude=message["location"]["latitude"],
        longitude=message["location"]["longitude"],
        city=message["location"]["city"],
        country=message["location"]["country"],
        person_id=person_id
    )

    insert_location(location)

    device_info = DeviceInfo(
        browser=message["device_info"]["browser"],
        os=message["device_info"]["os"],
        device_id=message["device_info"]["device_id"],
        person_id=person_id
    )

    insert_device_info(device_info)

    if destiny == 'hostage':
        sentences = [
            insert_hostage_content(SuspiciousHostageContent(
                sentence=sen,
                person_id = person_id
        ))
            for sen in message['sentences']
        ]

    if destiny == 'explosive':
        sentences = [
            insert_explosive_content(SuspiciousExplosiveContent(
                sentence=sen,
                person_id = person_id
        ))
            for sen in message['sentences']
        ]