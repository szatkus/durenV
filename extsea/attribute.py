import math

class Attribute(object):
	def __init__(self, name):
		self.name = name
		self.multi = 3
		self.rlevel = 1
		self.max_level = 255
		self.dep = []
		self.affect = []
		self.mod = None
		self.exp = 0
		self.atype = ""
	
	@property
	def bonus(self):
		self.tbonus = 1
		for d in self.dep:
			if isinstance(d, Attribute) and d.mod != None:
				d.mod(d, self)
		return self.tbonus
	
	@property
	def level(self):
		if self.rlevel > self.max_level:
			self.rlevel = self.max_level
		return self.rlevel*self.bonus
	
	@property
	def required(self):
		if self.rlevel < self.max_level:
			return math.pow(self.multi, self.rlevel)
		else:
			return -1
	
	@property
	def exp(self):
		return self.__exp
	
	@exp.setter
	def exp(self, exp):
		for d in self.dep:
			if isinstance(d, Attribute):
				d.exp += exp - self.__exp
		self.__exp = exp
		while self.required >= 0 and self.exp >= self.required:
			self.rlevel += 1
	
	def add(self, dep):
		if dep.name in self.dep:
			self.dep[self.dep.index(dep.name)] = dep
		else:
			self.dep.append(dep)


null_attrib = Attribute("none")
