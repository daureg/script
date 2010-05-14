#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable-msg=W0312
"""Update the version of a OLD_DIRectory by moving it."""
import sys, os

def print_help():
	"""Print the help of the script."""	
	print "\nUsage : updir [-M|-m|-r] [-h] directory"
	print "Incrémente la version du répertoire en entrée\n"
	print "\t -M\tincrémente le numéro majeur du répertoire"
	print "\t -m\tincrémente le numéro mineur du répertoire"
	print "\t -r\tincrémente le numéro de révision du répertoire"
	print "\t -h\taffiche cette aide"
	sys.exit()

def parse_dirname(dirname):
	"""Split 'dirname' into a name, and a {major,minor,revision} number."""
	name = ""
	version = range(3)
	version[0] = -1
	version[1] = -1
	version[2] = -1
	back = len(dirname)
	version_size = 0
	string_iteration = range(len(dirname))
	string_iteration.reverse()

	for i in string_iteration:
		if dirname[i] == '.':
			version_size += 1
		if dirname[i] == '-':
			version_size += 1
			break
	for j in string_iteration:
		if dirname[j] in ('.', '-'):
			version[version_size - 1] = dirname[j + 1:back]
			version_size -= 1
			back = j
		if version_size == 0:
			name = dirname[:j]
			break
	return name, version[0], version[1], version[2]

def up_dir(name, major, minor, rev, need_array):
	"""Update the directory name if needed."""
	new_dir = name + "-"
	if need_array[0]:
		if major == -1:
			print "ERROR: No major number in '%s' dirname" % name
			sys.exit()
		else:
			major = str(int(major) + 1)
	if major != -1:
		new_dir += major
	if need_array[1]:
		if minor == -1:
			print "ERROR: No minor number in '%s' dirname" % name
			sys.exit()
		else:
			minor = str(int(minor) + 1)

	if minor != -1:
		new_dir += '.' + minor
	if need_array[2]:
		if rev == -1:
			print "ERROR: No revision number in '%s' dirname" % name
			sys.exit()
		else:
			rev = str(int(rev) + 1)

	if rev != -1:
		new_dir += '.' + rev
	return new_dir

if __name__ == "__main__":
	UP_MAJOR = False
	UP_MINOR = False
	UP_REVISION = False
	OLD_DIR = ""
	for k in sys.argv:
		if k in ("-h", "--help"):
			print_help()
		if k == "-M":
			UP_MAJOR = True
		if k == "-m":
			UP_MINOR = True
		if k == "-r":
			UP_REVISION = True
		if k not in ("-h", "--help", "-M", "-m", "-r"):
			OLD_DIR = os.popen("basename " + k).read().strip()
	NEED_ARRAY = []
	NEED_ARRAY.append(UP_MAJOR)
	NEED_ARRAY.append(UP_MINOR)
	NEED_ARRAY.append(UP_REVISION)
	DIR_NAME, OLD_MAJOR, OLD_MINOR, OLD_REV = parse_dirname(OLD_DIR)
	NEW_DIR = up_dir(DIR_NAME, OLD_MAJOR, OLD_MINOR, OLD_REV, NEED_ARRAY)
	os.system("mv " + OLD_DIR + "/ " + NEW_DIR + "/")
	sys.exit()
