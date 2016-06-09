from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
session = None

''' verificar se o tipo period eh mesmo string '''
class WED_trigger(Base):
    __tablename__ = 'wed_trigger'
    id = Column(Integer, primary_key = True)
    active = Column(String(50))
    period = Column(String(50))
    wed_condition_id = Column(Integer, ForeignKey('wed_condition.id'))
    wed_condition = relationship("WED_condition", back_populates="wed_trigger")
