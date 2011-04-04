from attribute import *

class Character:
	
	def __init__(self, name):
		self.name = name
		self.attrib = {}
	
	def add(self, attrib):
		for name in self.attrib:
			iattrib = self.attrib[name]
			if iattrib.name in attrib.affect or attrib.name in iattrib.dep:
				iattrib.add(attrib)
			if attrib.name in iattrib.affect or iattrib.name in attrib.dep:
				attrib.add(iattrib)
		
		self.attrib[attrib.name] = attrib
	
	def find_attrib(self, atype):
		result = []
		for i in self.attrib:
			if self.attrib[i].atype == atype:
				result.append(self.attrib[i])
		if len(result) == 0:
			result = [null_attrib]
		return result
