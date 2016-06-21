from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Associations import *

''' olhar o site para fazer as relacoes, http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html'''
''' Aqui eu fiz uma relacao one to many bidirecional, tem que ver se e essa mesmo eu fiz mas eu nao sei a diferenca'''

class WED_condition(Base):
    __tablename__ = 'wed_condition'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    predicates = Column(String(50))
    expression = Column(String(50))
    wed_flow = relationship("WED_flow", back_populates="wed_condition")
    wed_trigger = relationship("WED_trigger", back_populates="wed_condition")
