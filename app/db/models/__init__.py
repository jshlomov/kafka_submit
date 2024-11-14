from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .PersonMessage import PersonMessage
from .Location import Location
from .DeviceInfo import DeviceInfo
from .SuspiciousHostageContent import SuspiciousHostageContent
from .SuspicionsExplosiveContent import SuspiciousExplosiveContent