from typing import Optional

from returns.maybe import Maybe
from sqlalchemy.exc import SQLAlchemyError

from app.db.models import PersonMessage, SuspiciousExplosiveContent, SuspiciousHostageContent
from app.db.postgres_db import session_maker
from returns.result import Result, Failure, Success



def insert_person(person: PersonMessage) -> Result[PersonMessage, str]:
    with session_maker() as session:
        try:
            session.add(person)
            session.commit()
            session.refresh(person)
            return Success(person)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def get_person_by_email(email) -> dict:
    with session_maker() as session:
        res = (
            session.query(PersonMessage)
            .filter(email == PersonMessage.email)
            .first()
        )
        return {
            "id": res.id,
            "email": res.email,
            "explosives": [sentece.sentence for sentece in res.explosive_contents],
            "hostages": [sentece.sentence for sentece in res.hostage_contents]
        }
