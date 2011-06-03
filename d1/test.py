from odisea import *
from extsea import *
import rpgdb

hero = Character("tester")
hero.add(rpgdb.create("strength"))
hero.add(rpgdb.create("human"))
hero.add(rpgdb.create("male"))
hero.add(rpgdb.create("life"))

game = Game({"patrz":look})

def cons(game):
	game.current = Place("start", 
	"""Punkt początkowy.
Tu zaczynamy""")
	def func(self, game):
		dialog("Jakaś tam popierdółka.")
	game.current.add(Object("Popierdółka", func))
	if not game.getb("niema"):
		def func(self, game):
			dialog("Znika...")
			game.tick("niema")
		game.current.add(Object("Coś", func))
	def func(self, game):
		if not game.getb("ruszone"):
			dialogd("Ruszyłem!")
			game.tick("ruszone")
		else:
			dialogd("Więcej nie grzebię")
	game.current.add(Object("Rucha", func))
game.add(cons)

game.state.go("start")
game.main_loop()
