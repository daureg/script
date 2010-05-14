#! /usr/bin/env python
# vim: fileencoding=utf-8 :
# pylint: disable-msg=W0312
# Author: Géraud Le Falher <daureg@gmail.com>
# Licence: GPL2 <http://www.opensource.org/licenses/gpl-2.0.php>
import sys, os
LISTE="/home/orphee/d/music/liste"
if __name__ == "__main__":
	song = sys.argv[1].split('/')[-1]
	found = False
	l = open(LISTE, 'r')
	liste = l.readlines()
	l.close()
	for i in range(len(liste)):
		if liste[i].find(song) != -1:
			n = int(liste[i].split(' ')[0])
			s = liste[i].split(' ')[1]
			liste[i] = "%s %s" %(str(n+1), s)
			found = True
	l = open(LISTE, 'w')
	for i in liste:
		l.write(i)
	if not found:
		l.write("1 %s\n"%song)
	l.close()
	sys.exit()
