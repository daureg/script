#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable-msg=W0312
""""""
import sys, os
if __name__ == "__main__":
	testing = os.popen("pacman -Sl testing|cut -d ' ' -f2").read().split()
	current = os.popen("pacman -Q|cut -d ' ' -f1").read().split()
	maybe_update = []
	testing_version = ""
	current_version = ""
	update = "sudo pacman -S"
	update_number = 0
	for i in current:
		if i in testing:
			maybe_update.append(i)
	for i in maybe_update:
		cmd = "pacman -Si testing/%s | grep '^Version' |cut -d ':' -f2"%i
		testing_version = os.popen(cmd).read().strip()
		cmd = "pacman -Q %s| cut -d ' ' -f2"%i
		current_version = os.popen(cmd).read().strip()
		if testing_version != current_version:
			update_number += 1
			update += " testing/" + i
			print i
			print testing_version
			print current_version
	print "%s testing update available"%str(update_number)
	if update_number:
		print update
	sys.exit()
