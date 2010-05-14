#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable-msg=W0312
"""Cherche mes paquets personnel installé dans ~/pkg."""
import sys, os

MAX_RECUR = 4
CURRENT_RECUR = 0
SAVE_DIR = os.environ['HOME'] + "/.pkg/"
GLOBAL = 0

def readdir(path, recur):
	"""Parcours recursivement 'path' (max 4) en cherchant des fichier PKGBUILD, pour
	les copier dans un autre dossier"""
	if recur < MAX_RECUR:
		for f in os.listdir(path):
			if os.path.isdir(path+os.sep+f):
				readdir(path+os.sep+f, recur+1)
			else:
				handle_dir(f, path)
def handle_dir(file, path):
	"""Effectue vraiment la copie"""
    	if file == "PKGBUILD":
		global GLOBAL
		GLOBAL = GLOBAL + 1
		dir = path.split('/')[4:]
		dir_str = '/'.join(dir)
		dir_str = SAVE_DIR + dir_str
		if not os.path.isdir(dir_str):
			os.makedirs(dir_str)
		os.chdir(path)
		os.popen("cp PKGBUILD %s"%dir_str)
		for extension in ['.install', '.desktop', '.png', '.patch', '.txt']:
			for filename in os.listdir(path):
				if filename.find(extension) != -1:
					os.popen("cp *%s %s"%(extension,dir_str))
		#Cas particulier
		if path.find("firefox-cvs") > 10:
			os.popen("cp mozconfig %s"%dir_str)
		if path.find("homer-kernel") > 10:
			os.popen("cp -r config update.sh %s"%dir_str)
		if path.find("scripts-perso") > 10:
			os.popen("cp -r scripts-perso* %s"%dir_str)

if __name__ == "__main__":
	pkg_dir = os.environ['HOME'] + "/pkg"
	readdir(pkg_dir, 0)
	os.popen("cp %s/desktop/xfce4-svn/{directory,build_xfce.py,mkVendor.sh} %s/desktop/xfce4-svn"%(pkg_dir,SAVE_DIR))
	print "%d dossiers traités"%GLOBAL
	sys.exit()

