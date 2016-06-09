from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
session = None

''' pessoal tem que rever essa classe, lah está att1, att2, attn....'''
class WED_state(Base):
    __tablename__ = 'wed_state'
    id = Column(Integer, primary_key = True)
    create_at = Column (DateTime)
    attribute = Column(String(50))
