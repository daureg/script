#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable-msg=W0312
import os, sys, random
"""Wrapper of cowsay"""
ALL = ['beavis.zen', 'bong', 'bud-frogs', 'bunny', 'cheese', 'cower', 'daemon', 'default', 'dragon-and-cow', 'dragon', 'elephant-in-snake', 'elephant', 'eyes', 'flaming-sheep', 'ghostbusters', 'head-in', 'hellokitty', 'kiss', 'kitty', 'koala', 'kosh', 'luke-koala', 'meow', 'milk', 'moofasa', 'moose', 'mutilated', 'ren', 'satanic', 'sheep', 'skeleton', 'small', 'sodomized', 'stegosaurus', 'stimpy', 'supermilker', 'surgery', 'telebears', 'three-eyes', 'turkey', 'turtle', 'tux', 'udder', 'vader-koala', 'vader', 'www']
BIG = ['cheese', 'daemon', 'dragon-and-cow', 'dragon', 'ghostbusters', 'kiss', 'ren', 'stegosaurus', 'stimpy', 'surgery', 'turkey', 'turtle']
EXP = ['head-in', 'kiss', 'sodomized', 'telebears']
NOR = ['bong', 'bud-frogs', 'cheese', 'daemon', 'default', 'dragon-and-cow', 'dragon', 'elephant', 'eyes', 'flaming-sheep', 'ghostbusters', 'meow', 'moofasa', 'moose', 'ren', 'sheep', 'skeleton', 'small', 'stegosaurus', 'surgery', 'three-eyes', 'turkey', 'turtle', 'tux', 'udder', 'vader', 'www']
QUT = ['bunny', 'hellokitty', 'kitty', 'koala', 'stimpy']
STR = ['beavis.zen', 'bong', 'cower', 'elephant-in-snake', 'kosh', 'luke-koala', 'milk', 'mutilated', 'satanic', 'supermilker', 'vader-koala']
#CMD = """cowsay -W 72 -f %s "\\"L'histoire d'une vie, quelle qu'elle soit, est l'histoire d'un échec.\\" - Jean-Paul Sartre, l'être et le néant" """
CMD = """cowsay -W 72 -f %s "%s" """
LIST = []
if sys.argv[1] not in ['a', 'b', 'e', 'n', 'q', 's']:
	print "Arg error, must b a|b|e|n|q|s"
	sys.exit()
else:
	if sys.argv[1] == 'a':
		LIST = ALL
	if sys.argv[1] == 'b':
		LIST = BIG
	if sys.argv[1] == 'e':
		LIST = EXP
	if sys.argv[1] == 'n':
		LIST = NOR
	if sys.argv[1] == 'q':
		LIST = QUT
	if sys.argv[1] == 's':
		LIST = STR
random.seed()
print os.popen(CMD % (LIST[random.randint(0,len(LIST)-1)], sys.argv[2])).read().strip()
