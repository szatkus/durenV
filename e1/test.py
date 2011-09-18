import extsea
import rpgdb

c = extsea.Character("elo")
print(c.name)

c.add(rpgdb.createl("sword", 4))
c.add(rpgdb.create("male"))
c.add(rpgdb.createl("strength", 3))
c.add(rpgdb.create("human"))

#rpgdb.viewc(c)

w = rpgdb.create_monster("wolf")
m = rpgdb.create_monster("mushroom")
w.team = 2
b = extsea.Battle([w, m])
b.run()
