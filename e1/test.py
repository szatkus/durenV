import extsea
import rpgdb

c = extsea.Character("elo")
print(c.name)

c.add(rpgdb.createl("sword", 4))
c.add(rpgdb.create("male"))
c.add(rpgdb.createl("strength", 3))
c.add(rpgdb.create("human"))
print(c.find_attrib("dupa")[0].name)

rpgdb.viewc(c)
