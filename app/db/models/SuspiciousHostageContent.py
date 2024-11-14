from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class SuspiciousHostageContent(Base):
    __tablename__ = "suspicious_hostage_content"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey("person_message.id"))

    person = relationship("PersonMessage", back_populates="hostage_contents")