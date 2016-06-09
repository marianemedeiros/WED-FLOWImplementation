from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
session = None

class WED_flow(Base):
    __tablename__ = 'wed_flow'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    wed_condition_id = Column(Integer, ForeignKey('wed_condition.id'))
    wed_condition = relationship("WED_condition", back_populates="wed_flow")