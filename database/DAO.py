from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from Associations import *
from History_entry import *
from Instance import *
from Interruption import *
from WED_condition import *
from WED_flow import *
from WED_state import *
from WED_transition import *
from WED_trigger import *
from Readxml import *
import settings

class DAO:

    def __init__(self):
        self.engine = create_engine(URL(**settings.DATABASE))
        self.readxml = Readxml('../xml/B1.xml')

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def insert(self):
            Session = sessionmaker(bind=self.engine)
            session = Session()  
            
            listConditions = self.readxml.data_wed_conditions();
            for condition in listConditions:
                session.add(condition)
            session.commit()

teste = DAO()
teste.insert()      