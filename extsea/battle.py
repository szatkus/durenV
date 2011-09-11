class Battle(object):
	'''Class for battle'''
	def __init__(self, char):
		'''Constructor
		char - list of characters which participate in a battle
		
		Example:
		b = Battle([character, rpgdb.create_monster('mushroom')])
		'''
		self.char = char
		self.time = 0
		self.max_ready = 1
		self.isrun = True
		self.log = []
		for char in self.char:
			char.log = self.log
			for a in char.attrib:
				char.attrib[a].log = self.log
			if "life" in char.attrib:
				char.life = char.max_life = char.attrib["life"].level
			if "speed" in char.attrib and char.attrib["speed"].level > self.max_ready:
				self.max_ready = char.attrib["speed"].level
			char.ready = 0
	
	def run(self):
		'''Runs a battle'''
		while self.isrun:
			for char in self.char:
				if "speed" in char.attrib:
					char.ready += char.attrib["speed"].level
					char.attrib['speed'].increase()
				if char.ready >= self.max_ready:
					char.ready -= self.max_ready
					if char.fight != None:
						char.fight(char, self)
			for char in self.char:
				if char.life <= 0:
					self.char.remove(char)
			team = self.char[0].team
			self.isrun = False
			for char in self.char:
				if char.team != team:
					self.isrun = True
	
	
