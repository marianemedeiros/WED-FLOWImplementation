from sqlalchemy import Integer, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Associations import *
from Instance import *
from WED_state import *
from Interruption import *
from WED_transition import *

<<<<<<< Updated upstream
engine = None
session = None
=======
Base = declarative_base()
>>>>>>> Stashed changes

class History_entry(Base):
    __tablename__ = 'history_entry'
    id = Column(Integer, primary_key = True)
    status = Column(String(50))
    consistent = Column(String(50))
    create_at = Column (DateTime)
    completed_at =  Column (DateTime)
<<<<<<< Updated upstream
    instance_id = Column(Integer, ForeignKey('instance.id'))
    instance = relationship("Instance", back_populates="history_entry")
    wed_state_id = Column(Integer, ForeignKey('wed_state.id'))
    wed_state = relationship("WED_state", back_populates="history_entry")
    interruption = relationship("Interruption", uselist=False, back_populates="history_entry")
    wed_transition_id = Column(Integer, ForeignKey('wed_transition.id'))
    wed_transition = relationship("WED_transition", back_populates="history_entry")
=======
>>>>>>> Stashed changes
