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

import settings

engine = create_engine(URL(**settings.DATABASE))

'''Base = declarative_base()'''

Base.metadata.create_all(engine)


'''
Exemplo de insercao de dados nas tabelas

Session = sessionmaker(bind=engine)

session = Session()

ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
ed_user_2 = User_2(identifier=1)
session.add(ed_user)
session.add(ed_user_2)
session.commit()

'''
