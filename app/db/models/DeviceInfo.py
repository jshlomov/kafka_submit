from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class DeviceInfo(Base):
    __tablename__ = "device_info"
    id = Column(Integer, primary_key=True, autoincrement=True)
    browser = Column(String, nullable=False)
    os = Column(String, nullable=False)
    device_id = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey("person_message.id"))

    person = relationship("PersonMessage", back_populates="device_info")