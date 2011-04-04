# -*- coding: utf-8 -*-

from odisea import *

def add(game):
	#Sklep
	def cons(state):
		state.name = "1shop"
		state.desc = """Jesteś w sklepie"""
		def func(self, state):
			dialog("No i co?")
		state.add(Object("Korytarz", func))
	game.add(cons)
