from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey("person.id"))

    persons = relationship("Person", back_populates="location")