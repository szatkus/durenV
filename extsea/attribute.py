import math

class Attribute(object):
	'''Class representing a single attribute.
	name - name
	title - displayed name (default same as name)
	multi - development multiplicator, if it's low the attribute 
	will develop faster (default 3)
	rlevel - basic level
	level - level after computing all depended attributes
	max_level - maximum level (default 255)
	dep - list of attribute on which attribute depend (but isn't required)
	affect - list of attributes which are affected by current attribute
	Warning: it's just second way to define dependencies between attributes,
	you shouldn't use both to create one link, i. e. when A.dep['Bname'],
	you shouldn't define B.affect['Aname']
	mod - function responsible for modify affected attributes. It's should
	two parameters, current attribute and affected attribute. During calling
	there is additional thing in affected attribute - tbonus. 
	Example:
	def human_mod(self, mod):
		if mod.name == 'life':
			mod.tbonus *= 10
		if mod.name == 'strength':
			mod.tbonus *= 4
		if mod.name == 'speed':
			mod.tbonus *= 5
	use_func - function called after use, should have 3 parameters, current
	attribute, using character and target character
	check - to be used in future
	exp - points of experience
	required - points required to level up
	atype - attribute type, for example 'gender', 'race', 'attack'
	log - history of actions with attribute
	'''
	def __init__(self, name):
		'''Constructor
		name - attribute's name'''
		self.name = name
		self.title = name
		self.multi = 3
		self.rlevel = 1 #Real level
		self.max_level = 255
		self.dep = []
		self.affect = []
		self.mod = None
		self.log = []
		self.use_func = None
		self.check = None
		self.exp = 0.0
		self.atype = '' #Ability type
		
	
	@property
	def bonus(self):
		self.tbonus = 1
		#print(self.dep)
		for d in self.dep:
			
			if isinstance(d, Attribute) and d.mod != None:
				
				d.mod(d, self)
		return self.tbonus
	
	@property
	def level(self):
		#print('a'+self.name)
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
		if self.required >= 0:
			self.log.append('exp %s %d'%(self.name, exp))
		while self.required >= 0 and self.exp >= self.required:
			self.rlevel += 1
			self.log.append('level %s %d'%(self.name, self.rlevel))
	
	def increase(self):
		'''Increase exp slightly'''
		self.exp += 1
	
	def use(self, user, target):
		'''Use an attribute.
		user - character which use an attribute
		target - character which is a target
		
		Example:
		herb.use(monk, geralt)'''
		self.log.append('use %s %s %s'%(self.name, user.name, target.name))
		self.use_func(self, user, target)
	
	def link(self, attribute):
		if self.name in attribute.affect:
			self.dep.append(attribute)
		if attribute.name in self.dep:
			self.dep[self.dep.index(attribute.name)] = attribute
		


null_attrib = Attribute("none")
