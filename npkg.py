#! /usr/bin/env python
# vim: fileencoding=utf-8 :
# pylint: disable-msg=W0312
"""Cherche mes paquets personnel installé dans ~/pkg."""
import sys, os, os.path, ConfigParser
from optparse import OptionParser

MAX_RECUR = 4
CURRENT_RECUR = 0

def get_packager():
	"""Get the packager name found in makepkf.conf"""
	return str(os.popen("cat /etc/makepkg.conf|grep PACKAGER|cut -c10-").read().strip().strip("\""))

def readdir(path, recur, install, ver_first):
	"""Parcours recursivement 'path' (max 4) en cherchant des fichier PKGBUILD, les 
	lits et verifier si le paquet est installé"""
	name = ''
	ver = ''
	url = ''
	if recur < MAX_RECUR:
		for f in os.listdir(path):
			if os.path.isdir(path+os.sep+f):
				readdir(path+os.sep+f, recur+1, install, ver_first)
			else:
				handle_file(f, install, ver_first, path)

def handle_file(file, install, ver_first, path):
	name = ''
	ver = ''
	url = ''
	packager = ''
	if file == "PKGBUILD":
		name, ver, url, packager = read_pkg(path+os.sep+file)
		if name in install and packager == get_packager():
			if ver_first:
				print ver + (13-len(ver))*" " + name + (28-len(name))*" " + url
			else:
				print name + (26-len(name))*" " + ver + (12-len(ver))*" "  + url

def read_pkg(file):
	"""Extract useful info of given PGKBUILD"""
	pkg = open(file)
	name = ''
	ver = ''
	url = ''
	packager = ''
	result = []
	for line in pkg:
		if line.find("Contributor") != -1:
			packager = line.split(':')[1].strip()
		if line.find("pkgname") == 0:
			name = line.strip().split('=')[1]
		if line.find("pkgver") == 0:
			ver = line.strip().split('=')[1]
		if line.find("url=\"") == 0:
			url  = line.strip().split('=\"')[1].strip('"')
	pkg.close()
	return name, ver, url, packager

if __name__ == "__main__":
	parser = OptionParser()
	parser.add_option("-d", "--directory", dest="start_dir",
		help="root directory to look")
	parser.add_option("-n", "--number", action="store_true", dest="first_version",
			default=False,	help="version of package first")
	(options, args) = parser.parse_args()

	INSTALL_ONE = os.popen("pacman -Q|cut -d ' ' -f-1").read()
	if os.path.exists(options.start_dir) == False:
		print options.start_dir + " doesn't seem to exist (check again)"
	readdir(options.start_dir, 0, INSTALL_ONE, options.first_version)
	sys.exit()

