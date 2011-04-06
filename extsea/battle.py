class Battle(object):
	#Constructor
	#char - a list of battle participants
	def __init__(self, char):
		self.char = char
		self.time = 0
		self.max_ready = 1
		self.isrun = True
		for char in self.char:
			if "life" in char.attrib:
				char.life = char.max_life = char.attrib["life"].level
			if "speed" in char.attrib and char.attrib["speed"].level > self.max_ready:
				self.max_ready = char.attrib["speed"].level
			char.ready = 0
	
	def run(self):
		while self.isrun:
			for char in self.char:
				if "speed" in char.attrib:
					char.ready += char.attrib["speed"].level
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
	
	
