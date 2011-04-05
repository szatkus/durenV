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
	
	#Life
	if name == "life":
		life = extsea.Attribute("life")
		life.atype = "ability"
		return(life)
	
	#Speed
	if name == "speed":
		speed = extsea.Attribute("speed")
		speed.atype = "ability"
		return(speed)
	
	#Sword
	if name == "sword":
		sword = extsea.Attribute("sword")
		sword.multi *= 4
		sword.dep = ["strength"]
		sword.atype = "skill"
		return(sword)
	
	#Human
	if name == "human":
		human = extsea.Attribute("human")
		human.affect = ["strength", "speed", "life"]
		human.max_level = 1
		def human_mod(self, mod):
			if mod.name == "life":
				mod.tbonus *= 10
			if mod.name == "strength":
				mod.tbonus *= 4
			if mod.name == "speed":
				mod.tbonus *= 5
		human.mod = human_mod
		human.atype = "race"
		return(human)
	
	#Wolf
	if name == "wolf":
		wolf = extsea.Attribute("wolf")
		wolf.affect = ["strength", "speed", "life"]
		wolf.max_level = 1
		def wolf_mod(self, mod):
			if mod.name == "life":
				mod.tbonus *= 8
			if mod.name == "strength":
				mod.tbonus *= 5
			if mod.name == "speed":
				mod.tbonus *= 7
		wolf.mod = wolf_mod
		wolf.atype = "race"
		return(wolf)
	
	#Mushroom
	if name == "mushroom":
		mushroom = extsea.Attribute("mushroom")
		mushroom.affect = ["strength", "speed", "life"]
		mushroom.max_level = 1
		def mushroom_mod(self, mod):
			if mod.name == "life":
				mod.tbonus *= 5
			if mod.name == "strength":
				mod.tbonus *= 2
			if mod.name == "speed":
				mod.tbonus *= 2
		mushroom.mod = mushroom_mod
		mushroom.atype = "race"
		return(mushroom)
		
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
	
	#Female
	if name == "female":
		female = extsea.Attribute("female")
		female.affect = ["speed", "magic"]
		female.max_level = 1
		def female_mod(self, mod):
			mod.tbonus *= 1.2
		female.mod = female_mod
		female.atype = "gender"
		return(female)
	
	#Bite
	if name == "bite":
		bite = extsea.Attribute("bite")
		bite.deps = ["strength"]
		def bite_use(self, mod):
			mod.tbonus *= 1.2
		bite.use = bite_use
		bite.atype = "attack"
		return(bite)
	
	return(None)

def createl(name, level):
	attrib = create(name)
	if attrib != None:
		attrib.rlevel = level
	return(attrib)


def create_monster(name):
	if name == "wolf":
		wolf = extsea.Character("Wolf")
		wolf.add(create("wolf"))
		wolf.add(createl("strength", 4))
		wolf.add(createl("speed", 4))
		wolf.add(createl("life", 4))
		return(wolf)
	
	if name == "mushroom":
		mushroom = extsea.Character("Mushroom")
		mushroom.add(create("mushroom"))
		mushroom.add(createl("strength", 4))
		mushroom.add(createl("speed", 4))
		mushroom.add(createl("life", 4))
		return(mushroom)
