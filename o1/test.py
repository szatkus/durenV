#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from odisea import *

game = Game(None)

def cons(game):
	game.current = Place("Start", """Początek gry

No...""")
	def testf(self, game):
		print(self.name)

	game.current.add(Object("Kostka", testf))
	game.current.add(Object("Świr", testf))

game.add(cons)
game.main_loop()
