from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database.Associations import *
from database.WED_flow import *
from database.WED_state import *
from database.Interruption import *
from database.History_entry import *

engine = None
session = None

class Instance(Base):
    __tablename__ = 'instance'
    id = Column(Integer, primary_key = True)
    status = Column(String(50))
    state_id = Column(Integer)
    create_at = Column (DateTime)
    finalized_at =  Column (DateTime)
    wed_flow_id = Column(Integer, ForeignKey('wed_flow.id'))
    wed_flow = relationship("WED_flow", back_populates="instance")
    #wed_state = relationship("WED_state", back_populates="instance")
    interruption = relationship("Interruption", back_populates="instance")
    history_entry = relationship("History_entry", back_populates="instance")


    # current_state_id = Column(Integer, ForeignKey('wed_state.id'))
    # current_state = relationship("WED_state", foreign_keys = [current_state_id])
