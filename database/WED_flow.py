from sqlalchemy import Integer, Column, create_engine, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database.Associations import *
from database.WED_condition import *
from database.Instance import *
from database.WED_trigger import *

engine = None
session = None

class WED_flow(Base):
    __tablename__ = 'wed_flow'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    final_condition = Column(Integer, ForeignKey('wed_condition.id')) #que eh wed_condition.id
    wed_condition = relationship("WED_condition", back_populates="wed_flow")
    instance = relationship("Instance", back_populates="wed_flow")
    wed_trigger = relationship("WED_trigger", back_populates="wed_flow")
