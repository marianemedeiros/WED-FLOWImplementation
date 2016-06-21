from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Associations import *
from WED_flow import *
from WED_trigger import *

engine = None
session = None
Base = declarative_base()

class WED_condition(Base):
    __tablename__ = 'wed_condition'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    predicates = Column(String(50))
    expression = Column(String(50))
    wed_flow = relationship("WED_flow", back_populates="wed_condition")
    wed_trigger = relationship("WED_trigger", back_populates="wed_condition")
	    	