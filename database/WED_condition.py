from sqlalchemy import Integer, Column, create_engine, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database.Associations import *

class WED_condition(Base):
    __tablename__ = 'wed_condition'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    predicates = Column(String(200))
    expression = Column(String(50))
    wed_flow = relationship("WED_flow", back_populates="wed_condition")
    wed_trigger = relationship("WED_trigger", back_populates="wed_condition")
