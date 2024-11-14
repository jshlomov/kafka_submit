from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.models import Base


class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey("person_message.id"))

    person_message = relationship("PersonMessage", back_populates="location")