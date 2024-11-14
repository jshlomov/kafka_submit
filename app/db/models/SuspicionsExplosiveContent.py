from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class SuspiciousExplosiveContent(Base):
    __tablename__ = "suspicious_explosive_content"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey("person_message.id"))

    person_message = relationship("PersonMessage", back_populates="explosive_contents")