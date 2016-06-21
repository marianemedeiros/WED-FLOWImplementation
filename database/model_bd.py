from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
session = None

class WED_condition(Base):
    __tablename__ = 'wed_condition'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    predicates = Column(String(50))
    expression = Column(String(50))
    awic = (Boolean)
    wed_flow = relationship("WED_flow", back_populates="wed_condition")
    wed_trigger = relationship("WED_trigger", back_populates="wed_condition")

class WED_flow(Base):
    __tablename__ = 'wed_flow'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    wed_condition_id = Column(Integer, ForeignKey('wed_condition.id'))
    wed_condition = relationship("WED_condition", back_populates="wed_flow")

''' verificar se o tipo period eh mesmo string '''
class WED_trigger(Base):
    __tablename__ = 'wed_trigger'
    id = Column(Integer, primary_key = True)
    active = Column(String(50))
    period = Column(String(50))
    wed_condition_id = Column(Integer, ForeignKey('wed_condition.id'))
    wed_condition = relationship("WED_condition", back_populates="wed_trigger")


class WED_transition(Base):
    __tablename__ = 'wed_transition'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))


class Instance(Base):
    __tablename__ = 'instance'
    id = Column(Integer, primary_key = True)
    status = Column(String(50))
    create_at = Column (DateTime)
    finalized_at =  Column (DateTime)

class Interruption(Base):
    __tablename__ = 'interruption'
    id = Column(Integer, primary_key = True)
    status = Column(String(50))
    consistent = Column(String(50))
    create_at = Column (DateTime)
    recovered_at =  Column (DateTime)

class History_entry(Base):
    __tablename__ = 'history_entry'
    id = Column(Integer, primary_key = True)
    status = Column(String(50))
    consistent = Column(String(50))
    create_at = Column (DateTime)
    completed_at =  Column (DateTime)

class WED_state(Base):
    __tablename__ = 'wed_state'
    id = Column(Integer, primary_key = True)
    create_at = Column (DateTime)
    attribute = Column(String(50))
