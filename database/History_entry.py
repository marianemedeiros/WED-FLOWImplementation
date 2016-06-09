from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
session = None

class History_entry(Base):
    __tablename__ = 'history_entry'
    id = Column(Integer, primary_key = True)
    status = Column(String(50))
    consistent = Column(String(50))
    create_at = Column (DateTime)
    completed_at =  Column (DateTime)