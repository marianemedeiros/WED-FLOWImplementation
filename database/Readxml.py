import xmltodict

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
		#print(d)
		return d

	def data_wed_transitions(self):
		d = dict()
		d = self.dict_xml['WED-flow-initial-schema']['WED-transitions']
		#print(d)
		return d

	def data_wed_flows(self):
		d = dict()
		d = self.dict_xml['WED-flow-initial-schema']['WED-flows']
		#print(d)
		return d

	def data_wed_AWICs(self):
		d = dict()
		d = self.dict_xml['WED-flow-initial-schema']['AWICs']
		#print(d)
		return d
