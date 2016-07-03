import sys
import xmltodict

import database.Associations
from database.Interruption import Interruption
from database.History_entry import History_entry
from database.Instance import Instance
from database.WED_attribute import WED_attribute
from database.WED_condition import WED_condition
from database.WED_flow import WED_flow 
from database.WED_transition import WED_transition
from database.WED_trigger import WED_trigger

class Readxml:

    def __init__(self, path_file_xml):
        xml_file = open(path_file_xml)
        self.dict_xml = xmltodict.parse(xml_file.read())
        self.dao = None
        self.initial_state = dict()

    def alter_table_state(self, attributes):
        data = ''
        for attr in attributes:
            if attr == attributes[-1]:
                if(attr.type_ == 'string'):
                    data = data + '    ' + attr.name + '= Column(' + attr.type_.title() + '(50))'
                else:
                    data = data + '    ' + attr.name + '= Column(' + attr.type_.title() + ')'
            elif(attr.type_ == 'string'):
                data = data + '    ' + attr.name + '= Column(' + attr.type_.title() + '(50))\n'
            else:
                data = data + '    ' + attr.name + '= Column(' + attr.type_.title() + ')\n'

        #print(data)

        state_file = open('database/WED_state.py', 'r')
        data_file = state_file.read()
        #favor nao retirar o tab da string abaixo
        new_data = data_file.replace('    attribute = Column(String(50))', data)
        state_file.close()

        state_file = open('database/WED_state.py', 'w')
        state_file.write(new_data)


        state_file.close()

    def data_wed_attributes(self):
        d = dict()
        d = self.dict_xml['WED-flow-initial-schema']['WED-attributes']['Attribute']
        list_obj_attr = list()
        for data_attributes in d:
            name = data_attributes['@Name']
            type_ = data_attributes['@Type']
            if(len(data_attributes) > 2):
                inicial_id = data_attributes['@inicial_id']
                inicial_value = data_attributes['@inicial_value']
                self.initial_state[inicial_id] = inicial_value

            wed_attributes = WED_attribute(name=name, type_=type_)
            list_obj_attr.append(wed_attributes);

        Readxml.alter_table_state(self,list_obj_attr)
        return list_obj_attr, self.initial_state

    def set_dao(self, dao):
        self.dao = dao

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
                    #pred = pred + text['#text'] + ","
            else:
                pred = "- " + predicates['#text'].replace(" = ",",").replace("\"","") + ",="
                #pred = predicates['#text']
            
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
            attributes = list()
            name = data_transitions['@Name']
            up_att = data_transitions['UpdatedAttribute']
            if isinstance(up_att, list):
                attrname = ''
                for att in up_att:
                    attrname = attrname + att['@AttrName'] + ' '
                    attributes.append(att['@AttrName'])
            else:
                attrname = (up_att['@AttrName'])
                attributes.append(up_att['@AttrName'])

            #print(name)
            #print(attributes)
            # Readxml.generate_class(name, attributes)

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
            result = self.dao.select_condition(wed_condition)
            final_condition  = result[0].id
            wed_flow = WED_flow(name = name, final_condition =final_condition)
            list_obj_flow.append(wed_flow)
        return list_obj_flow

# transition
    # bloqueia o estado atual na instancia. bloqueia na tabela de wed_state o instance_id2
    # cria um novo estado
    # atualiza estado atual no Instance e libera o bloqueio
    # atualiza o history_entry (monitor passa a linha do history)
    # Inserir o novo estado nas filas
    def generate_class(name, attributes):
        strAtt = ''
        for att in attributes:
            if len(attributes) == 1:
                strAtt = att + ':' + att
            else:
                strAtt = strAtt + att + ':\'' + att + '\', '
                if att == attributes[-1]:
                    strAtt = strAtt + att + ':\'' + att + '\''

        body_class =   'class '+ name +'():\n'\
                     + '    def run():\n'\
                     + '        return {'+strAtt+'}'
        #print(body_class)
        file = open('transitions/'+name+'.py','w')
        file.write(body_class)
        file.close()

    def data_wed_trigger(self):
        d = dict()
        d = self.dict_xml['WED-flow-initial-schema']['WED-flows']
        list_obj_trigger = list()
        for data_flows in d:
            result_flow = self.dao.select_flow(d['Flow']['@Name'])
            flow_id = result_flow[0].id
            triggers = d['Flow']['Trigger']
            for tgg in triggers:
                result_cond_id = self.dao.select_condition(tgg['@CondName'])
                cond_id = result_cond_id[0].id
                result_trans_id = self.dao.select_transition(tgg['@TransName'])
                trans_id = result_trans_id[0].id
                period  = tgg['@Period']
                period = int(period[0])
                wed_trigger = WED_trigger( wed_condition_id = cond_id, wed_transition_id = trans_id, wed_flow_id = flow_id, active ='TRUE' , period = period)
                list_obj_trigger.append(wed_trigger)
        return list_obj_trigger

#teste = Readxml('../xml/B1.xml')
#teste.data_wed_attributes()
