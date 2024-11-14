from sqlalchemy.exc import SQLAlchemyError

from app.db.models import PersonMessage
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