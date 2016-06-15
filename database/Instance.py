from sqlalchemy import Integer, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Associations import *
from WED_flow import *
from WED_state import *
from Interruption import *
from History_entry import *

<<<<<<< Updated upstream
engine = None
session = None
=======
Base = declarative_base()
>>>>>>> Stashed changes

class Instance(Base):
    __tablename__ = 'instance'
    id = Column(Integer, primary_key = True)
    status = Column(String(50))
    create_at = Column (DateTime)
    finalized_at =  Column (DateTime)
<<<<<<< Updated upstream
    wed_flow_id = Column(Integer, ForeignKey('wed_flow.id'))
    wed_flow = relationship("WED_flow", back_populates="instance")
    wed_state = relationship("WED_state", back_populates="instance")
    interruption = relationship("Interruption", back_populates="instance")
    history_entry = relationship("History_entry", back_populates="instance")

=======
>>>>>>> Stashed changes
