"""Odysea adventure engine main module
"""

from Game import *

version = "0.0.2"

def look(game):
	"""Look action. Only attach to an object"""
	game.state.look()

def stop(game):
	"""Stop action. Only attach to an object"""
	game.stop()

def dialog(d):
	"""Shows a dialog message"""
	print(d)

def isay(d):
	"""Say something"""
	print("["+d+"]")
	input()

def say(a, d):
	"""Say something"""
	print(a+": ["+d+"]")
	input()

def dialogd(d):
	"""Shows a dialog message and waits"""
	print(d)
	input()

def message(m):
	"""Shows a system message"""
	print(m)

def menu(title, item):
	"""Shows menu.
	title - The title of the menu. It's displayed over menu.
	item - List of menu items"""
	result = -1
	while result == -1:
		print(title)
		nr = 1
		for i in item:
			print("%d. %s"%(nr, i))
			nr = nr+1
		try:
			result = int(cmd)
			if result < 1 or result >= nr:
				result = -1
		except:
			pass
	return result
