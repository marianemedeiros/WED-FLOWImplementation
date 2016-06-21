from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Associations import *
from WED_condition import *
from Instance import *
from WED_trigger import *

engine = None
session = None

class WED_flow(Base):
    __tablename__ = 'wed_flow'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    wed_condition_id = Column(Integer, ForeignKey('wed_condition.id'))
    wed_condition = relationship("WED_condition", back_populates="wed_flow")
    instance = relationship("Instance", back_populates="wed-flow")
    wed_trigger = relationship("WED_trigger", back_populates="wed_flow")
