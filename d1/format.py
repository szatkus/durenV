#To nie jest plik Pythona!
@start
Punkt początkowy.
Tu zaczynamy.
	>Popierdółka
		dialog("Jakaś tam popierdółka.")
	if not game.getb("niema"):
		>Coś
			dialog("Znika...")
			game.tick("niema")
	>Rucha
		if not game.getb("ruszone"):
			dialogd("Ruszyłem!")
			game.tick("ruszone")
		else:
			dialogd("Więcej nie grzebię")
