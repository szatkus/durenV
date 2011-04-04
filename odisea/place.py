# -*- coding: utf-8 -*-


def del_pl(s):
	"""Helper that replaces polish charachters"""
	s = s.replace("ś", "s")
	s = s.replace("Ś", "S")
	s = s.replace("ć", "c")
	s = s.replace("Ć", "C")
	s = s.replace("ł", "l")
	s = s.replace("Ł", "L")
	s = s.replace("ń", "n")
	s = s.replace("Ń", "N")
	s = s.replace("ą", "a")
	s = s.replace("Ą", "A")
	s = s.replace("ę", "e")
	s = s.replace("Ę", "E")
	s = s.replace("ó", "o")
	s = s.replace("Ó", "O")
	s = s.replace("ź", "z")
	s = s.replace("Ź", "Z")
	s = s.replace("ż", "z")
	s = s.replace("Ż", "Z")
	return s

class Place:
	"""Place class (TO REMOVE)"""
	def __init__(self, name, desc):
		self.name = name
		self.desc = desc
		self.obj = {}
	
	def add(self, obj):
		self.obj[obj.name] = obj;
	
	def remove(self, obj):
		del self.obj[obj.name];
	
	def find(self, name):
		name = del_pl(name)
		name = name.lower()
		for i in self.obj:
			pattern = i
			pattern = del_pl(pattern)
			pattern = pattern.lower()
			if pattern == name:
				return self.obj[i]
