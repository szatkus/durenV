from .attribute import *
import random

class Character:
	'''Class representing a character
	fight - battle controller, it's just a function with two parameters,
	current character and battle. It's called everytime character have to act
	during battle. For example look into rpgdb.ai_dumb source.'''
	def __init__(self, name):
		'''Constructor
		name - name of character
		
		Example:
		geralt = Character('Geralt')
		'''
		self.name = name
		self.attrib = {}
		self.life = 0
		self.max_life = 0
		self.ready = 0
		self.team = 1
		self.fight = None
	
	def add(self, attrib):
		'''Adds an attribute
		attrib - attribute to be attached
		
		Example:
		geralt.add(rpgdb.create('strength'))'''
		for name in self.attrib:
			iattrib = self.attrib[name]
			if iattrib.name in attrib.affect or attrib.name in iattrib.dep:
				iattrib.add(attrib)
			if attrib.name in iattrib.affect or iattrib.name in attrib.dep:
				attrib.add(iattrib)
		
		self.attrib[attrib.name] = attrib
	
	def find_attrib(self, atype):
		'''Find attributes of specific type
		atype - ability type
		returns - list of attributes
		
		Example:
		attacks = geralt.find_attrib('attack')
		'''
		result = []
		for i in self.attrib:
			if self.attrib[i].atype == atype:
				result.append(self.attrib[i])
		if len(result) == 0:
			result = [null_attrib]
		return result
	
	def damage(self, dmg):
		'''Deal damage to character
		This lower character's life, but also add exp to life attribute
		dmg - amount of damage
		
		Example:
		geralt.damage(2)
		'''
		dmg = (0.5+random.random())*dmg
		self.life -= dmg
		if 'life' in self.attrib:
			life = self.attrib['life']
			life.exp += dmg/life.level
		return dmg
