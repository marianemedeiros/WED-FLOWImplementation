from sqlalchemy import Integer, Column, create_engine, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Associations import *
from WED_flow import *
from WED_state import *
from WED_transition import *
from WED_condition import *

engine = None
session = None

''' verificar se o tipo period eh mesmo string '''
class WED_trigger(Base):
    __tablename__ = 'wed_trigger'
    id = Column(Integer, primary_key = True)
    active = Column(String(50))
    period = Column(String(50))
    wed_flow_id = Column(Integer, ForeignKey('wed_flow.id'))
    wed_flow = relationship("WED_flow", back_populates="wed_trigger")
    wed_state = relationship("WED_state", secondary=wedState_wedTrigger, back_populates="wed_trigger")
    wed_transition_id = Column(Integer, ForeignKey('wed_transition.id'))
    wed_transition = relationship("WED_transition", back_populates="wed_trigger")
    wed_condition_id = Column(Integer, ForeignKey('wed_condition.id'))
    wed_condition = relationship("WED_condition", back_populates="wed_trigger")
