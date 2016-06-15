from sqlalchemy import Integer, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Associations import *
from Instance import *
from History_entry import *

<<<<<<< Updated upstream
engine = None
session = None
=======
Base = declarative_base()
>>>>>>> Stashed changes

class Interruption(Base):
    __tablename__ = 'interruption'
    id = Column(Integer, primary_key = True)
    status = Column(String(50))
    consistent = Column(String(50))
    create_at = Column (DateTime)
    recovered_at =  Column (DateTime)
    instance_id = Column(Integer, ForeignKey('instance.id'))
    instance = relationship("Instance", back_populates="interruption")
    history_entry_id = Column(Integer, ForeignKey('history_entry.id'))
    history_entry = relationship("History_entry", back_populates="interruption")
