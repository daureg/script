#! /usr/bin/env python
# vim: fileencoding=utf-8 :
#pylint: disable-msg=W0312
"""Search the list of package which start from specified letter."""
import sys, string, os
COMMAND = "pacman -Q|grep "
if len(sys.argv) != 2:
	print "Bad number of arguments, just one !"
	sys.exit()
else:
	ARG = sys.argv[1]
if len(ARG) not in [1, 2] or ARG[0] not in string.ascii_lowercase:
	print "Bad arguments, just one or two letters !"
	sys.exit()

if len(ARG) == 1:
	if ARG == 'l':
		COMMAND += "'^l'|grep -v '^lib'|column" 
	else:
		COMMAND += "'^" + ARG + "'|column"
else:
	if ARG[0] != 'l':
		print "Two-letters argument must begin by a l"
		sys.exit()
	else:
		COMMAND += "'^lib" + ARG[1] + "'|column"
print os.popen(COMMAND).read()
