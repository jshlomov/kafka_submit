from sqlalchemy.exc import SQLAlchemyError

from app.db.models import DeviceInfo
from app.db.postgres_db import session_maker
from returns.result import Result, Failure, Success



def insert_device_info(device_info: DeviceInfo) -> Result[DeviceInfo, str]:
    with session_maker() as session:
        try:
            session.add(device_info)
            session.commit()
            session.refresh(device_info)
            return Success(device_info)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))