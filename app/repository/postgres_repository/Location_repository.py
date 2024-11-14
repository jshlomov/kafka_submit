from sqlalchemy.exc import SQLAlchemyError

from app.db.models import Location
from app.db.postgres_db import session_maker
from returns.result import Result, Failure, Success



def insert_location(location: Location) -> Result[Location, str]:
    with session_maker() as session:
        try:
            session.add(location)
            session.commit()
            session.refresh(location)
            return Success(location)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))