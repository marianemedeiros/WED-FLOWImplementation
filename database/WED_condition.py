from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
session = None

''' olhar o site para fazer as relações, http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html'''
''' Aqui eu fiz uma relação one to many bidirecional, tem que ver se é essa mesmo eu fiz mas eu não sei a diferença'''
class WED_condition(Base):
    __tablename__ = 'wed_condition'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    predicates = Column(String(50))
    expression = (String(50))
    awic = (Boolean)
    wed_flow = relationship("WED_flow", back_populates="wed_condition")
    wed_trigger = relationship("WED_trigger", back_populates="wed_condition")