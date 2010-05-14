#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable-msg=W0312
"""Cherche mes paquets personnel installé dans ~/pkg."""
#chercher plutot les PKGBUILD et en extraire pkgname, pkgver, url
import sys, os
if __name__ == "__main__":
	INSTALL_ONE = os.popen("pacman -Q|cut -d ' ' -f-1").read()
	PRE_MY = os.popen('ls -RfF \
			~/pkg/{admin,devel,desktop,graphics,games,lib,net,science,sound}\
		|grep "/$"|	grep -v "\./$\|-base/$\|tmp/$\|^.svn\|props/$"').read().strip('/')
	for i in PRE_MY.split():
		i = i.strip('/')
		if i in INSTALL_ONE:
			print i
	sys.exit()
