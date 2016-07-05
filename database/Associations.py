from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, Session

Base = declarative_base()

class wedState_wedTrigger(Base):
    __tablename__ = 'wedState_wedTrigger'
    wed_state_id = Column(Integer, ForeignKey('wed_state.id'), primary_key=True)
    wed_trigger_id = Column(Integer, ForeignKey('wed_trigger.id'), primary_key=True)
    status = Column(String(50))

    wed_state = relationship("WED_state", back_populates="wed_trigger")
    wed_trigger = relationship("WED_trigger", back_populates="wed_state")
