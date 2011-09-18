#!/bin/python
# -*- coding: utf-8 -*-

from odisea import *
import sys
import part1

selected = 1#menu("Witaj!", ["Nowa gra", "Wyjdz"])

if selected == 2:
	message("Do zobaczenia!")

def inventory(game):
	print("Ekwipunek:")
	items = {"key":"Klucz", "lighter":"Zapalniczka"}
	for i in items:
		if game.state.getb(i):
			print(items[i])

def helpme(game):
	print("patrz")	
	print("przedmioty")
	print("pomoc")
	print("koniec")

if selected == 1:
	game = Game({"patrz":look, "koniec":stop, "pomoc":helpme, "help":helpme, "przedmioty":inventory})
	
	#Pokój 1
	def cons(game):
		game.current = Place("your_room", 
		"""Jestem we własnym pokoju.
Dookoła burdel jak zwykle.""")
		game.check_var("your_room", 0)
		game.check_var("devil", False)
		if game.db["devil"]:
			game.db["your_room"] = 2
		if game.db["your_room"] == 0:
			def func(self, game):
				if not game.getb("door1"):
					dialog("Zamknięte.")
					game.db["door1"] = True
				else:
					dialog("Zbyt solidne, żeby próbować sforsować.")
			game.current.add(Object("Drzwi", func))
			def func(self, game):
				dialog("Nie działa internet.") 
			game.current.add(Object("Komputer", func))
			def func(self, game):
				dialog("Za oknem jest... mur?")
			game.current.add(Object("Okno", func))
			def func(self, game):
				dialogd("W szafie widzisz jakieś światło. Zbliżasz się do niego.")
				dialogd("Szafa jest głębsza niż myślałeś.")
				game.go("closet")
			game.current.add(Object("Szafa", func))
		if game.db["your_room"] == 1:
			def func(self, game):
				game.go("corridorn1")
			game.current.add(Object("Drzwi", func))
			def func(self, game):
				dialog("Wszystko działa, ale nie masz teraz czasu.") 
			game.current.add(Object("Komputer", func))
			def func(self, game):
				dialog("Za oknem ładna pogoda.")
			game.current.add(Object("Okno", func))
			def func(self, game):
				dialog("W szafie nie ma nic ciekawego")
			game.current.add(Object("Szafa", func))
		if game.db["your_room"] == 2:
			def func(self, game):
				game.go("corridorn1")
			game.current.add(Object("Drzwi", func))
			def func(self, game):
				dialog("Nie działa.") 
			game.current.add(Object("Komputer", func))
			def func(self, game):
				dialog("Za oknem pustka.")
			game.current.add(Object("Okno", func))
			if not game.getb("lighter"):
				def func(self, game):
					game.go("closet2")
				game.current.add(Object("Szafa", func))
	game.add(cons)
	
	#Szafa
	def cons(game):
		game.current = Place("closet", 
		"""Jesteś w środku szafy.""")
		def func(self, game):
			dialogd("Wychodzisz na korytarz...")
			game.go("corridor1")
		game.current.add(Object("Światło", func))
		def func(self, game):
			dialog("Za tobą nic nie ma.")
		game.current.add(Object("Wróć", func))
	game.add(cons)
	
	#Szafa normalna
	def cons(game):
		game.current = Place("closet2", 
		"""Jesteś w środku szafy.""")
		def func(self, game):
			if game.getb("lighter"):
				dialogd("Ubrania stają w płomieniach.")
				dialog("Drzwi się odblokowały. Wychodzisz")
				game.go("corridorn1")
			else:
				dialog("Znajdujesz zapalniczkę")
				game.db["lighter"] = True
		game.current.add(Object("Ubrania", func))
		def func(self, game):
			dialog("Coś trzyma drzwi.")
		game.current.add(Object("Wyjście", func))
	game.add(cons)
	
	#Korytarz1
	def cons(game):
		game.current = Place("corridor1", 
		"""Jesteś przed wejściem do swojego pokoju.""")
		def func(self, game):
			dialog("Zamknięte.")
		game.current.add(Object("Drzwi", func))
		def func(self, game):
			game.go("corridor2")
		game.current.add(Object("Korytarz", func))
	game.add(cons)
	
	#Korytarz2
	def cons(game):
		game.current = Place("corridor2", 
		"""Jesteś na korytarzu.""")
		def func(self, game):
			game.go("corridor3")
		game.current.add(Object("Korytarz", func))
		if not game.getb("key"):
			def func(self, game):
				dialog("Podniosłeś klucz")
				game.db["key"] = True
			game.current.add(Object("Klucz", func))
	game.add(cons)
	
	#Korytarz3
	def cons(game):
		game.current = Place("corridor3", 
		"""Jesteś na korytarzu. Na ścianie wisi zdjęcie.""")
		def func(self, game):
			game.go("corridor4")
		game.current.add(Object("Korytarz", func))
		def func(self, game):
			game.check_var("key", False)
			dialog("Za ramką jest dziurka od klucza")
			if game.db["key"]:
				dialogd("Klucz nie pasuje.")
				dialogd("Ale dziurka się rozpada.")
				dialogd("Wchodzisz w otwór w ściane.")
				dialogd("Wychodzisz ze szafy.")
				game.db["your_room"] = 1
				game.go("your_room")
		game.current.add(Object("Ramka", func))
	game.add(cons)
	
	#Korytarz4
	def cons(game):
		game.current = Place("corridor4", 
		"""Jesteś na korytarzu.""")
		def func(self, game):
			game.go("corridor2")
		game.current.add(Object("Korytarz", func))
	game.add(cons)
	
	#Korytarz normalny 1
	def cons(game):
		game.current = Place("corridorn1", 
		"""Jesteś przed wejściem do swojego pokoju.""")
		def func(self, game):
			if game.getb("lighter"):
				dialog("W środku jest pożar.")
			else:
				game.go("your_room")
		game.current.add(Object("Drzwi", func))
		def func(self, game):
			game.go("corridorn2")
		game.current.add(Object("Korytarz", func))
	game.add(cons)
	
	#Korytarz normalny 2
	def cons(game):
		game.current = Place("corridorn2", 
		"""Jesteś przy schodach na dół""")
		def func(self, game):
			if game.getb("bed_burnt"):
				dialog("W środku jest pożar.")
			else:
				game.go("parents_room")
		game.current.add(Object("Drzwi", func))
		def func(self, game):
			game.go("corridorn1")
		game.current.add(Object("Korytarz", func))
		def func(self, game):
			game.go("bathroom")
		game.current.add(Object("Łazienka", func))
		def func(self, game):
			game.tick("devil")
			game.go("lounge")
		game.current.add(Object("Schody", func))
	game.add(cons)
	
	#Salon
	def cons(game):
		if game.getb("theend"):
			desc = "Jestem w salonie."
		else:
			desc = "W salonie jest wody po kolana."
		game.current = Place("lounge", desc)
		def func(self, game):
			if game.getb("theend"):
				dialog("Nie dam rady uciec.")
			else:
				game.go("corridorn2")
		game.current.add(Object("Góra", func))
		if game.getb("lighter") and game.getb("handle") and game.getb("bed_burnt"):
			def func(self, game):
				if game.getb("theend"):
					dialog("Lepiej wymyślę jak go pokonać...")
				else:
					say("Demon", "To już koniec...")
					isay("To się nie może tak skończyć!")
					say("Demon", "Twoje wysiłki poszły na marne. Najlepiej poddaj się od razu.")
					game.tick("theend")
			game.current.add(Object("Demon", func))
		if game.getb("theend"):
			def func(self, game):
				dialog("Nie czas się wylegiwać.")
			game.current.add(Object("Kanapa", func))
			if not game.getb("carpet"):
				def func(self, game):
					dialogd("Podpaliłem dywan.")
					dialog("Ale demona to nie rusza.")
					game.tick("carpet")
				game.current.add(Object("Dywan", func))
			def func(self, game):
				dialogd("Mam pasujący klucz.")
				dialogd("Za drzwiami jest jasne światło.")
				say("Demon", "Po co to robisz? Przedłużasz tylko swoje męki.")
				dialogd("Wchodzę w światło.")
				dialogd(".")
				dialogd("..")
				dialogd("...")
				dialogd("Jestem w samym środku sklepu...")
				dialogd("Ta sytuacja... To już kiedyś było...")
				dialogd("Dałem siostrze prezent urodzinowy i niedługo potem poszedłem na zakupy...")
				dialogd("Ona poszła do domu i po powrocie rozpakowała go...")
				dialogd("Tak, teraz pamiętam...")
				dialogd("Muszę ją powstrzymać!")
				game.go("1shop")
			game.current.add(Object("Drzwi", func))
		else:
			def func(self, game):
				dialogd("Wchodzę do wody...")
				dialogd("Okazało się głębiej niż myślałem, tonę.")
				dialog("Udało mi się złapać poręczy schodów i wyjść.")
			game.current.add(Object("Woda", func))
	game.add(cons)
	
	#Pokój rodziców
	def cons(game):
		game.current = Place("parents_room", 
		"""Jesteś w pokoju rodziców""")
		def func(self, game):
			dialog("Nie działa.")
		game.current.add(Object("Telewizor", func))
		def func(self, game):
			if game.getb("bad_bed") and game.getb("lighter"):
				dialogd("Podpalasz łózko")
				dialog("Lepiej się stąd wynosić")
				game.tick("bed_burnt")
				game.go("corridorn2")
			else:
				game.tick("devil")
				game.tick("bad_bed")
				dialogd("Kładziesz się na łóżku...")
				dialogd("Zaczyna cię wciągać!")
				dialog("Udaje ci się wydostać.")
		game.current.add(Object("Łóżko", func))
		def func(self, game):
			game.go("corridorn2")
		game.current.add(Object("Drzwi", func))
	game.add(cons)
	
	#Łazienka
	def cons(game):
		game.current = Place("bathroom", 
		"""Jesteś w łazience.""")
		def func(self, game):
			game.tick("devil")
			dialog("Nie widzę własnego odbicia?")
		game.current.add(Object("Lustro", func))
		def func(self, game):
			dialog("Umyłem ręce.")
		game.current.add(Object("Umywalka", func))
		def func(self, game):
			dialog("Nie potrzebuje tego.")
		game.current.add(Object("Sedes", func))
		def func(self, game):
			if game.getb("handle"):
				dialog("Kabina jest rozbita.")
			else:
				dialogd("Wchodzę do kabiny.")
				dialogd("Coś zamyka mnie w środku.")
				game.go("cabin")
		game.current.add(Object("Kabina", func))
		def func(self, game):
			game.go("corridorn2")
		game.current.add(Object("Drzwi", func))
	game.add(cons)
	
	def cons(game):
		game.current = Place("cabin", 
		"""Wnętrze kabiny.""")
		def func(self, game):
			if game.getb("shower"):
				dialog("Nie daje się zakręcić.")
			else:
				dialogd("Odkręciłem prysznic.")
				dialog("Kabina powoli napełnia się wodą i jest wyjątkowo szczelna.")
				game.tick("shower")
		game.current.add(Object("Prysznic", func))
		if not game.getb("handle"):
			def func(self, game):
				if game.getb("try_handle"):
					dialogd("Jest już trochę poluzowany.")
					dialog("Wyrwałem uchwyt.")
					game.tick("handle")
				else:
					dialog("Nie mogę wyrwać.")
					game.tick("try_handle")
			game.current.add(Object("Uchwyt", func))
		def func(self, game):
			if game.getb("handle"):
				dialogd("Rozbiłem ścianę kabiny uchwytem.")
				game.go("bathroom")
			else:
				dialog("Coś trzyma drzwi.")
		game.current.add(Object("Wyjście", func))
	game.add(cons)
	
	part1.add(game)
	
	game.state.go("your_room")
	
	if len(sys.argv) > 1:
		game.state.load(sys.argv[1])
		game.autosave = sys.argv[1]
	
	game.main_loop()
