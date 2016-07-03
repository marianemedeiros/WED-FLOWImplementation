from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from database.Associations import *


engine = None
session = None

class History_entry(Base):
    __tablename__ = 'history_entry'
    id = Column(Integer, primary_key = True)
    status = Column(String(50))
    create_at = Column (DateTime)
    completed_at =  Column (DateTime)
    instance_id = Column(Integer, ForeignKey('instance.id'))
    instance = relationship("Instance", back_populates="history_entry")

    initial_state_id = Column(Integer, ForeignKey('wed_state.id'))
    current_state_id = Column(Integer, ForeignKey('wed_state.id'))

    initial_state = relationship("WED_state", foreign_keys = [initial_state_id])
    current_state = relationship("WED_state", foreign_keys = [current_state_id])


    final_state_id = Column(Integer, ForeignKey('wed_state.id'))
    final_state = relationship("WED_state", foreign_keys = [final_state_id])

  
    interruption = relationship("Interruption", uselist=False, back_populates="history_entry")
    wed_transition_id = Column(Integer, ForeignKey('wed_transition.id'))
    wed_transition = relationship("WED_transition", back_populates="history_entry")