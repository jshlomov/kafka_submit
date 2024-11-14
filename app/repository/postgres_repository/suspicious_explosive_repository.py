from sqlalchemy.exc import SQLAlchemyError

from app.db.models import SuspiciousExplosiveContent, SuspiciousHostageContent, PersonMessage
from app.db.postgres_db import session_maker
from returns.result import Result, Failure, Success



def insert_explosive_content(explosive_content: SuspiciousExplosiveContent) -> Result[SuspiciousExplosiveContent, str]:
    with session_maker() as session:
        try:
            session.add(explosive_content)
            session.commit()
            session.refresh(explosive_content)
            return Success(explosive_content)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))