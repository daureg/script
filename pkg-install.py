#! /usr/bin/env python
# vim: fileencoding=utf-8 :
# pylint: disable-msg=W0312
# Author: Géraud Le Falher <daureg@gmail.com>
# Licence: GPL2 <http://www.opensource.org/licenses/gpl-2.0.php>
"""Update a pacman package in the current by removing the potentiel conflict."""
import sys, os
if __name__ == "__main__":
	pkg = os.popen("ls -t|grep pkg.tar.xz|head -n 1").read().strip()[:-16]
	new = '-'.join(pkg.split('-')[:-2])
	conf = '-'.join(new.split('-')[:-1])
	os.popen("sudo pacman -Rd %s"%conf)
	os.popen("sudo pacman -U %s-i686.pkg.tar.xz"%pkg)
