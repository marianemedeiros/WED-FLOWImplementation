from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base
from Associations import *
from Instance import *
from WED_state import *
from Interruption import *
from WED_transition import *

engine = None
session = None

class History_entry(Base):
    __tablename__ = 'history_entry'
    id = Column(Integer, primary_key = True)
    status = Column(String(50))
    consistent = Column(String(50))
    create_at = Column (DateTime)
    completed_at =  Column (DateTime)
    instance_id = Column(Integer, ForeignKey('instance.id'))
    instance = relationship("Instance", back_populates="history_entry")
    wed_state_id = Column(Integer, ForeignKey('wed_state.id'))
    wed_state = relationship("WED_state", back_populates="history_entry")
    interruption = relationship("Interruption", uselist=False, back_populates="history_entry")
    wed_transition_id = Column(Integer, ForeignKey('wed_transition.id'))
    wed_transition = relationship("WED_transition", back_populates="history_entry")