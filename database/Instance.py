from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
session = None

class Instance(Base):
    __tablename__ = 'instance'
    id = Column(Integer, primary_key = True)
    status = Column(String(50))
    create_at = Column (DateTime)
    finalized_at =  Column (DateTime)

