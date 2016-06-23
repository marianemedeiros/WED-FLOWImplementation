from sqlalchemy import Integer, Column, create_engine, ForeignKey, String
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from Associations import *
from History_entry import *
from WED_trigger import *

engine = None
session = None

class WED_transition(Base):
    __tablename__ = 'wed_transition'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    history_entry = relationship("History_entry", back_populates="wed_transition")
    wed_trigger = relationship("WED_trigger", back_populates="wed_transition")
