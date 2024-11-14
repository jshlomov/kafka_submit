from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class PersonMessage(Base):
    __tablename__ = "person_message"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    created_at = Column(String, nullable=False)

    location = relationship("Location", back_populates="person_message", uselist=False)
    device_info = relationship("DeviceInfo", back_populates="person_message", uselist=False)
    explosive_contents = relationship("SuspiciousExplosiveContent", back_populates="person_message")
    hostage_contents = relationship("SuspiciousHostageContent", back_populates="person_message")