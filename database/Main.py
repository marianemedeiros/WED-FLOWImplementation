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
from DAO import *
import settings

dao = DAO()
dao.drop_tables()
dao.create_tables()
#dao.insert_wed_conditions()
