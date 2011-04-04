from place import *

class GameState(Place):
	def __init__(self):
		self.db = {}
		self.current = None
		self.place = None
		self.name = ""
		self.desc = ""
	
	def check_var(self, name, default):
		"""Check if var exists"""
		if not name in self.db:
			self.db[name] = default
	
	def getb(self, name):
		"""Get boolean value from database.
If value doesn't exists its default value is False."""
		self.check_var(name, False)
		return self.db[name]
	
	def refresh(self):
		"""Refresh game state"""
		if self.place != None:
			self.place(self)
			self.align()
	
	def align(self):
		"""Backward compatibility."""
		if self.current != None:
			self.name = self.current.name
			self.desc = self.current.desc
			self.obj = self.current.obj
		self.current = None
	
	def tick(self, name):
		"""Set True"""
		self.db[name] = True
	
	def go(self, name):
		"""Go to another location"""
		self.name = name
	
	def look(self):
		"""Print current location description."""
		self.refresh()
		print(self.desc)
		for i in self.obj:
			print("*"+self.obj[i].name)
	
	def save(self, filename):
		"""Save game state to file"""
		f = open(filename, 'w')
		if not f.closed:
			f.write(self.name+"\n"+str(self.db))
		else:
			print("Can't save file "+filename)
			print("Disabling an autosave")
			self.autosave = ""
	
	def load(self, filename):
		"""Load game state from file"""
		try:
			f = open(filename, 'r')
			s = f.readline().strip()
			self.quiet = True
			self.go(s)
			self.quiet = False
			self.db = eval(f.readline())
			f.close()
		except:
			print("Can't load file "+filename)
