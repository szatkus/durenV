from .attribute import *
import random

class Character:
	'''Class representing a character
	fight - battle controller, it's just a function with two parameters,
	current character and battle. It's called everytime character have to act
	during battle. For example look into rpgdb.ai_dumb source.
	log - history of actions done by character'''
	def __init__(self, name):
		'''Constructor
		name - name of character
		
		Example:
		geralt = Character('Geralt')
		'''
		self.name = name
		self.attrib = {}
		self.trash = {}
		self.life = 0
		self.max_life = 0
		self.ready = 0
		self.team = 1
		self.fight = None
		self.log = []
	
	def __unicode__(self):
		return self.name
		
	def __str__(self):
		return 'ExtseaCharacter: '+self.name
	
	def add(self, attrib):
		'''Adds an attribute
		attrib - attribute to be attached
		
		Example:
		geralt.add(rpgdb.create('strength'))'''
		for name in self.attrib:
			iattrib = self.attrib[name]
			iattrib.link(attrib)
			attrib.link(iattrib)
		
		self.attrib[attrib.name] = attrib
		self.log.append('add %s %s'%(self.name, attrib.name))
					
	
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
		self.log.append('damage %s %d'%(self.name, dmg))
		return dmg
