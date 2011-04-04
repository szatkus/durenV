from object import *
from place import *
from gamestate import *
from sys import *

class Game:
	"""Main game class"""	
	
	def __init__(self, main):
		"""The only argument is a dictionary of commands-functions.
Functions have to have one argument - game class."""
		self.main = main
		self.place = {}
		self.run = True
		self.autosave = ""
		self.quiet = False
		self.state = GameState()
	
	def stop(self):
		"""Stop main loop"""
		self.run = False
	
	def add(self, place_cons):
		"""Add new place constructor"""
		place_cons(self.state)
		print(self.state.name)
		self.state.align()
		
		self.place[self.state.name] = place_cons;
	
	def main_loop(self):
		"""Main loop"""
		self.run = True
		name = ""
		while self.run:
			try:
				if name != self.state.name:
					name = self.state.name
					if self.state.name in self.place:
						self.state.place = self.place[self.state.name]
						self.state.refresh()
						
					else:
						print("Place "+self.state.name+" doesn't exist")
					self.state.look()
					if self.autosave != "":
						self.state.save(self.autosave)
				self.state.refresh()
				stdout.write("> ")
				cmd = raw_input()
				cmd = cmd.lower()
				
				if cmd in self.main:
					self.main[cmd](self)
				else:
					obj = self.state.find(cmd)
					if obj != None:
						obj.func(obj, self.state)
					else:
						print("Nie znaleziono")
			except EOFError:
				self.run = False;
			
