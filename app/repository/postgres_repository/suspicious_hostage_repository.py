from sqlalchemy.exc import SQLAlchemyError

from app.db.models import SuspiciousExplosiveContent
from app.db.postgres_db import session_maker
from returns.result import Result, Failure, Success



def insert_hostage_content(hostage_content: SuspiciousExplosiveContent) -> Result[SuspiciousExplosiveContent, str]:
    with session_maker() as session:
        try:
            session.add(hostage_content)
            session.commit()
            session.refresh(hostage_content)
            return Success(hostage_content)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))