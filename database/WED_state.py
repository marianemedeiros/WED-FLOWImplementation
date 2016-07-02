from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from database.Associations import *


''' pessoal tem que rever essa classe, lah esta att1, att2, attn....'''
class WED_state(Base):
    __tablename__ = 'wed_state'
    id = Column(Integer, primary_key = True)
    id_cliente= Column(Integer)
    cliente= Column(String(50))
    pontos= Column(Integer)
    id_produto= Column(Integer)
    produto= Column(String(50))
    id_pedido= Column(Integer)
    pedido= Column(String(50))
    pagamento= Column(String(50))

    instance_id = Column(Integer, ForeignKey('instance.id'))
    instance = relationship("Instance", foreign_keys=[instance_id])

    instance_id2 = Column(Integer, ForeignKey('instance.id'))
    instance2 = relationship("Instance", foreign_keys=[instance_id2])

    wed_trigger = relationship("WED_trigger", secondary=wedState_wedTrigger, back_populates="wed_state")
    
