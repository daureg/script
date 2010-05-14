#! /usr/bin/env python
# -*- coding: utf-8 -*-
#pylint: disable-msg=W0312
"""Update the $pkgver of a svn PKGBUILD"""
import sys, os, time

def get_svn_version(f):
	"""Get the new svn version."""
	trunk = ""
	old = 0
	new = 0
	for line in f:
		if line.find("pkgver") == 0:
			old = int(line.strip().split('=')[1])
		if line.find("_svntrunk=") == 0:
			trunk = line.strip().split('=')[1]
	new = int(os.popen("""svn log %s --limit 1 -q | sed -n 's/^r\([0-9]*\) .*$/\\1/p'"""%trunk).read().strip())
	return trunk, old, new

def get_svn_log(trunk, old, new):
	"""Return the svn log of 'trunk' between revision 'old' and 'new'."""
	return os.popen("svn log --non-interactive %s -r%s:%s"%(trunk, str(old+1), str(new))).read().strip()

def write_log(old, new):
	"""Write the svn log to a report file."""
	date = time.strftime("%Y-%m-%d %H:%M", time.gmtime())
	report = "%s "%(date) + ": %s -> %s\n"%(str(old), str(new))
	report += get_svn_log(trunk, old, new) + "\n"
	f = open("svn_log", 'a')
	f.write(report)
	f.close()

def sed_pkgbuild(old, new):
	"""Replace the old $pkgver by the new using sed"""
	cmd = "sed -i s/%s/%s/g PKGBUILD"%(str(old), str(new))
	os.popen(cmd)

if __name__ == "__main__":
	report = ""
	trunk = ""
	old = 0
	new = 0

	PKG = open("PKGBUILD", 'r')
	trunk, old, new = get_svn_version(PKG)
	if new > old:
		print ("%s -> %s"%(str(old), str(new)))
		write_log(old, new)
		sed_pkgbuild(old, new)
	else:
		print("Already up to date")
	sys.exit()


