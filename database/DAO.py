import datetime
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.Readxml import *
import database.settings
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from database.Associations import wedState_wedTrigger
from database.Interruption import Interruption
from database.History_entry import History_entry
from database.Instance import Instance
from database.WED_attribute import WED_attribute
from database.WED_condition import WED_condition
from database.WED_flow import WED_flow 
from database.WED_transition import WED_transition
from database.WED_trigger import WED_trigger
from database.Readxml import Readxml
from database.WED_state import WED_state

# from database.settings import *

class DAO:

    def __init__(self):
        self.engine = create_engine(URL(**database.settings.DATABASE))
        #self.readxml = Readxml('../xml/B1.xml')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()    
        self.readxml = None

    def __del__(self):
        self.session.close_all()
        self.engine

    def set_readxml(self, readxml):
        self.readxml = readxml

    def create_tables(self):
        #Base.metadata.create_all(self.engine)
        WED_attribute.__table__.create(self.engine)
        WED_condition.__table__.create(self.engine)
        WED_transition.__table__.create(self.engine)
        WED_flow.__table__.create(self.engine)
        WED_trigger.__table__.create(self.engine)
        Instance.__table__.create(self.engine)
        #tabelas history e instance serao criadas depois da wed_state
        #History_entry.__table__.create(self.engine)
        #Interruption.__table__.create(self.engine)
        #wedState_wedTrigger

    def drop_tables(self):
        wedState_wedTrigger.__table__.drop(self.engine)
        Interruption.__table__.drop(self.engine)
        History_entry.__table__.drop(self.engine)
        WED_state.__table__.drop(self.engine)
        Instance.__table__.drop(self.engine)
        WED_trigger.__table__.drop(self.engine)
        WED_flow.__table__.drop(self.engine)
        WED_transition.__table__.drop(self.engine)
        WED_condition.__table__.drop(self.engine)
        WED_attribute.__table__.drop(self.engine)

    def insert(self):
        list_attributes = self.readxml.data_wed_attributes()
        for attributes in list_attributes[0]:
            self.session.add(attributes)
            self.session.commit()

        list_conditions = self.readxml.data_wed_conditions()
        for condition in list_conditions:
            self.session.add(condition)
            self.session.commit()        

        list_transitions = self.readxml.data_wed_transitions()
        for transitions in list_transitions:
            self.session.add(transitions)
            self.session.commit()
                                
        list_flows = self.readxml.data_wed_flows()
        for flows in list_flows:
            self.session.add(flows)
            self.session.commit()        

        list_trigger = self.readxml.data_wed_trigger()
        for trigger in list_trigger:
            self.session.add(trigger)
            self.session.commit()    

        # depois de ler os wed_attributes cria a tabela wed_state, como History tem relacionamento com
        # wed-state, entao cria ele depois do wed_state e Interruption tem relacionamento com
        # History entao cria tbn.
        DAO.create_necessary_tables(self)

        #self.insert_wed_state(list_attributes)

    def insert_wed_state(self,list_attributes):
        #1 criar um instance
        #2 cria state
        wed_flow = DAO.select_flow(self)
        instance = DAO.create_instance(self,"started",wed_flow[0].id)

        #TODO o certo certo messsmo é nesta parte fazer de acordo com o wed_attribute, ou seja,
        #ler o wed_attribute colocar na lista o nome , o id e o valor.
        initial_state = WED_state(id_cliente=1, cliente=list_attributes[1]["1"], id_produto=2, produto=list_attributes[1]["2"], instance_id=instance.id)
        self.session.add(initial_state)
        self.session.commit()
        instance.state_id = initial_state.id;
        self.session.commit()

    def create_instance(self,status_,wed_flow_id,finalized_at=None):
        if(finalized_at == None):
            instance = Instance(status=status_, create_at=datetime.datetime.now(), wed_flow_id=wed_flow_id)
            self.session.add(instance)
        else:
            instance = Instance(status=status_, create_at=datetime.datetime.now(), finalized_at=finalized_at,wed_flow_id=wed_flow.id)
            self.session.add(instance)
        self.session.commit()
        return instance

    def create_necessary_tables(self):
        WED_state.__table__.create(self.engine)
        History_entry.__table__.create(self.engine)
        Interruption.__table__.create(self.engine)
        wedState_wedTrigger.__table__.create(self.engine)

    def select_condition(self, wed_condition = None):
        if wed_condition == None:
            result = self.session.query(WED_condition).all()
        else:
            result = self.session.query(WED_condition).filter_by(name = wed_condition).all()
        return result

    def select_transition(self, wed_transition = None):
        if wed_transition == None:
            result = self.session.query(WED_transition).all()
        else:
            result = self.session.query(WED_transition).filter_by(name = wed_transition).all()
        return result

    def select_flow(self, wed_flow = None):
        if wed_flow == None:
            result = self.session.query(WED_flow).all()
        else:
            result = self.session.query(WED_flow).filter_by(name = wed_flow).all()
        return result 

    def select_trigger(self):
        return self.session.query(WED_trigger).all()

    def select_fila(self, trigger_id):
        return self.session.query(wedState_wedTrigger).with_for_update().filter_by\
                (wed_trigger_id = trigger_id, status = "started").all()

    def select_state(self, state_id):
        return self.session.query(WED_state).filter_by(id = state_id).all()

    # def select_condition(self, condition_id):
    #     return self.session.query(WED_condition).filter_by(id = condition_id)

    def select_wedflow2(self, wedflow_id):
        return self.session.query(WED_flow).filter_by(id=wedflow_id).all()

    def select_instance(self, instance_id):
        return self.session.query(Instance).filter_by(id = instance_id).all()
