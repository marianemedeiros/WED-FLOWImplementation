from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from Readxml import *
import settings

class DAO:

    def __init__(self):
        self.engine = create_engine(URL(**settings.DATABASE))
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
        #tabelas history e instance será criadas depois da wed_state
        #History_entry.__table__.create(self.engine)
        #Interruption.__table__.create(self.engine)

        #wedState_wedTrigger

    def drop_tables(self):
        Base.metadata.drop_all(self.engine)

    def insert(self):
        list_attributes = self.readxml.data_wed_attributes()
        for attributes in list_attributes:
            self.session.add(attributes)
            self.session.commit()

        # depois de ler os wed_attributes cria a tabela wed_state, como History tem relacionamento com
        # wed-state, entao cria ele depois do wed_state e Interruption tem relacionamento com
        # History entao cria tbn.
        DAO.create_necessary_tables(self)
        
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

    def create_necessary_tables(self):
        WED_state.__table__.create(self.engine)
        History_entry.__table__.create(self.engine)
        Interruption.__table__.create(self.engine)
        wedState_wedTrigger.create(self.engine)
  
    def select_condition(self, wed_condition):
        result = self.session.execute(
            "SELECT id FROM wed_condition WHERE name = '" + wed_condition + "'"
        ).fetchone()
        return result

    def select_transition(self, wed_transition):
        result = self.session.execute(
            "SELECT id FROM wed_transition WHERE name = '" + wed_transition + "'"
        ).fetchone()
        return result

    def select_flow(self, wed_flow):
        result = self.session.execute(
            "SELECT id FROM wed_flow WHERE name = '" + wed_flow + "'"
        ).fetchone()
        return result        
#dao = DAO()
#b = Readxml('../xml/B1.xml')
#dao.set_readxml(b)
#dao.drop_tables
#dao.insert()
#print(dao.select_test('c_pedido_finalizado'))
# listResult = dao.select_test()
# for l in listResult:
#     print(l[0])