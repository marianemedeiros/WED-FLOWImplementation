import xmltodict
from model_bd import *
import settings


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
                    pred = pred + text['#text']
            else:
                pred = predicates['#text']
            expression = data_conditions['Expression']
            wed_condition = WED_condition(name=name, predicates=pred, expression=expression)
            list_obj_cond.append(wed_condition);
        return list_obj_cond

    def data_wed_transitions(self):
        d = dict()
        d = self.dict_xml['WED-flow-initial-schema']['WED-transitions']        


        return d

    def data_wed_flows(self):
        d = dict()
        d = self.dict_xml['WED-flow-initial-schema']['WED-flows']['Flow']
        list_obj_cond = list()
        for data_flows in d:
            
        #print(d)
        return d

    def data_wed_AWICs(self):
        d = dict()
        d = self.dict_xml['WED-flow-initial-schema']['AWICs']
        #print(d)
        return d

teste = Readxml('../xml/B1.xml')
teste.data_wed_conditions()