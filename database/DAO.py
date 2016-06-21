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
        dict_data = self.readxml.data_wed_conditions()
        for name in dict_data:
            print(name['@Name'])
            #print(name['Predicate'])
            
            predicates = name['Predicate']
            if isinstance(predicates, list):
                for text in predicates:
                    '''cliente = "invalido" '''
                    '''- cliente,invalido,='''
                    vetor = "- " + text['#text'].replace(" = ",",").replace("\"","") + ",="
                    print(vetor)
            else:
                print(predicates['#text'])

            expression = name['Expression']
            #print (expression)
            if("AND" in expression):
                expr = expression.replace(" AND "," ") + " and"
            elif("OR" in expression):
                expr = expression.replace(" OR "," ") + " or"
            else:
                expr = expression

            print("-- " + expr)

            Session = sessionmaker(bind=self.engine)
            session = Session()  
            
            wed_condition = WED_condition(name=name['@Name'], predicates=vetor, expression=expr)
            #wed_flow = WED_flow(name="teste",wed_condition=wed_condition);
            session.add(wed_condition)
            session.commit()

teste = DAO()
teste.insert()      