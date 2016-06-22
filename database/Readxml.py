import xmltodict
from WED_condition import *
from WED_flow import *
from WED_state import *
from WED_transition import *
from WED_trigger import *

class Readxml:

    def __init__(self, path_file_xml):
        xml_file = open(path_file_xml)
        self.dict_xml = xmltodict.parse(xml_file.read())

    def data_wed_attributes(self):
        d = dict()
        d = self.dict_xml['WED-flow-initial-schema']['WED-attributes']['Attribute']
        #print(d)       
        return d

    def data_wed_conditions(self):
        d = dict()
        d = self.dict_xml['WED-flow-initial-schema']['WED-conditions']['Condition']
        list_obj_cond = list()
        for data_conditions in d:
            name = data_conditions['@Name']          
            predicates = data_conditions['Predicate']
            if isinstance(predicates, list):
                pred = ''
                for text in predicates:
                    pred = pred + "- " + text['#text'].replace(" = ",",").replace("\"","") + ",=" 
            else:
                pred = "- " + predicates['#text'].replace(" = ",",").replace("\"","") + ",="
            
            expression = data_conditions['Expression']

            if("AND" in expression):
                expr = expression.replace(" AND "," ") + " and"
            elif("OR" in expression):
                expr = expression.replace(" OR "," ") + " or"
            else:
                expr = expression

            wed_condition = WED_condition(name=name, predicates=pred, expression=expr)
            list_obj_cond.append(wed_condition);
        return list_obj_cond

    def data_wed_transitions(self):
        d = dict()
        d = self.dict_xml['WED-flow-initial-schema']['WED-transitions']['Transition']    
        list_obj_transition = list()
        for data_transitions in d:
            name = data_transitions['@Name']
            print(name)
            up_att = data_transitions['UpdatedAttribute']
            if isinstance(up_att, list):
                attrname = ''
                for att in up_att:
                    attrname = attrname + att['@AttrName'] + ' '
            else:
                attrname = (up_att['@AttrName'])

            wed_transition = WED_transition(name=name)
            list_obj_transition.append(wed_transition)
        return list_obj_transition

    def data_wed_flows(self):
        d = dict()
        d = self.dict_xml['WED-flow-initial-schema']['WED-flows']
        list_obj_flow = list()
        for data_flows in d:
            name = d['Flow']['@Name']
            wed_condition = d['Flow']['@FinalStateCondName']
            triggers = d['Flow']['Trigger']
            for tgg in triggers:
                print(tgg['@CondName'])
                print(tgg['@TransName'])
                print(tgg['@Period'])
            # dao = DAO()
            # result = dao.select_test()
            # final_condition  = result[0]
            #wed_flow = WED_flow(name = name, final_condition = final_condition)
            #list_obj_flow.append(wed_flow)
        return list_obj_flow

#teste = Readxml('../xml/B1.xml')
# teste.data_wed_flows()