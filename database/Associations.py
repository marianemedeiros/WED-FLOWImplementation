from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, Session

Base = declarative_base()

#class wedState_wedTrigger(Base):
#    __tablename__ = 'wedState_wedTrigger'
wedState_wedTrigger = Table('wedState_wedTrigger', Base.metadata,
    #wed_state_id = Column(Integer, ForeignKey('wed_state.id'), primary_key=True)
    #wed_trigger_id = Column(Integer, ForeignKey('wed_trigger.id'), primary_key=True)
    #status = Column(String(50))
    Column('wed_state_id', Integer, ForeignKey('wed_state.id'), primary_key=True),
    Column('wed_trigger_id', Integer, ForeignKey('wed_trigger.id'), primary_key=True),
    Column('status', String(50))
)
