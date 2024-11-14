from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .Person import Person
from .Location import Location
from .DeviceInfo import DeviceInfo
from .SuspiciousHostageContent import SuspiciousHostageContent
from .SuspicionsExplosiveContent import SuspiciousExplosiveContent