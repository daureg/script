#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
from time import strftime, gmtime

def get_new_version(pkgname,pkgfile,current_version):
	method = get_update_method(pkgname)
	if method == "release":
		new = raw_input("New release number ?")
		return new
	if method == "svn":
		trunk = get_value_from_file(pkgfile, "_svntrunk", "=")
		cmd = "wget -O index " + trunk
		print cmd
		os.system(cmd)
		file = open("index","r")
		for line in file:
			if line_contain_svn_revision(line):
				return extract_svn_revision(line)
		error("New SVN revision, not found ! You must fill the PKGBUILD by hand")
	if method == "cvs" or method == "git" or method == "darcs":
		return strftime("%Y%m%d",gmtime())

def error(msg):
	print "\t--ERROR : "+msg
	sys.exit()

def get_value_from_file(file, value_name, separator) :
	file.seek(0,0)
	for line in file :
		sub = line.find(value_name)
		pos = line.find(separator)
		if(sub != -1 and pos != -1 and line[0] != '#'):
			return line[pos+1:len(line)]

def get_update_method(pkgname):
	if pkgname.find("cvs") != -1:
                return "cvs"
        if pkgname.find("svn") != -1:
                return "svn"
        if pkgname.find("git") != -1:
                return "git"
        if pkgname.find("darcs") != -1:
                return "darcs"
        else:
                return "release"

def get_information(pkgfile) :
	info = {}
	info['pkg']=get_value_from_file(pkgfile,"pkgname","=")
	info['rel']=get_value_from_file(pkgfile,"pkgrel","=")
	info['old']=get_value_from_file(pkgfile,"pkgver","=")	
	info['new']=get_new_version(info['pkg'],pkgfile,info['old'])
	info['arch']=get_proc_arch(pkgfile)
	return info

pkg = open("PKGBUILD", "r")
print get_information(pkg)
pkg.close()
