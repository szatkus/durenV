import extsea

def view(a):
	print(a.name)
	print(a.level)
	print("%d/%d"%(a.exp, a.required))

def viewc(c):
	print(c.name)
	for n in c.attrib:
		a = c.attrib[n]
		print("%d(%d) %s"%(a.rlevel, a.level, a.name))

def create(name):
	#Strength
	if name == "strength":
		strength = extsea.Attribute("strength")
		def strength_mod(self, mod):
			mod.tbonus *= self.level
		strength.mod = strength_mod
		strength.atype = "ability"
		return(strength)
	
	#Sword
	if name == "sword":
		sword = extsea.Attribute("sword")
		sword.dep = ["strength"]
		sword.atype = "skill"
		return(sword)
	
	#Human
	if name == "human":
		human = extsea.Attribute("human")
		human.affect = ["strength", "speed"]
		human.max_level = 1
		def human_mod(self, mod):
			mod.tbonus *= 5
		human.mod = human_mod
		human.atype = "race"
		return(human)
		
	#Male
	if name == "male":
		male = extsea.Attribute("male")
		male.affect = ["strength", "life"]
		male.max_level = 1
		def male_mod(self, mod):
			mod.tbonus *= 1.2
		male.mod = male_mod
		male.atype = "gender"
		return(male)
	
	return(None)

def createl(name, level):
	attrib = create(name)
	if attrib != None:
		attrib.rlevel = level
	return(attrib)


