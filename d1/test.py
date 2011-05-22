import odisea
import extsea
import rpgdb

hero = extsea.Character("tester")
hero.add(rpgdb.create("strength"))
hero.add(rpgdb.create("human"))
hero.add(rpgdb.create("male"))
hero.add(rpgdb.create("life"))

prompt = ">"
run = True

while run:
	cmd = input()
	if cmd == "quit":
		run = False
