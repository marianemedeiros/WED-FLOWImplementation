from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from Associations import *
from Instance import *
from WED_trigger import *
from History_entry import *

engine = None
session = None

''' pessoal tem que rever essa classe, lah esta att1, att2, attn....'''
class WED_state(Base):
    __tablename__ = 'wed_state'
    id = Column(Integer, primary_key = True)
    create_at = Column (DateTime)
    id_cliente= Column(Integer)
    cliente= Column(String(50))
    pontos= Column(Integer)
    id_produto= Column(Integer)
    produto= Column(String(50))
    id_pedido= Column(Integer)
    pedido= Column(String(50))
    pagamento= Column(String(50))
    instance_id = Column(Integer, ForeignKey('instance.id'))
    instance = relationship("Instance", back_populates="wed_state")
    wed_trigger = relationship("WED_trigger", secondary=wedState_wedTrigger, back_populates="wed_state")
    history_entry = relationship("History_entry", uselist=False, back_populates="wed_state")
