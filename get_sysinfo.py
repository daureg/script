#! /usr/bin/python2
# vim: fileencoding=utf-8 :
# pylint: disable-msg=W0312
import os, sys
info = sys.argv[1]
if len(sys.argv) > 2:
	distro = sys.argv[2]
else:
	distro="archlinux"

if distro=="archlinux":
	DISKS=['sda9']
else:
	DISKS=['sda8']
SOMME=False

def get_mail():
	import libgmail
	ga = libgmail.GmailAccount("daureg@gmail.com", MOTDEPASSE)
	ga.login()
	return ga.getUnreadMsgCount()

if info == "mail":
	import time
	interval = int(sys.argv[2])
	if int(time.time()) % interval == 0:
		print "%s"%get_mail()
	else:
		print "*"

if info == "uptime":
	print os.popen("uptime").read().split()[2].strip(',')

if info == "cpu_temp":
	temp = os.popen("sensors|grep Core|cut -d '+' -f2|cut -c -4").read().strip().split()
	r=0.0
	for i in temp:
		r=r+float(i)
	print "%.1f°C"%(r/len(temp))


if info == "disk_free":
	if SOMME:
		res=0
		for i in DISKS:
			res = res + int(os.popen("df|grep %s"%i).read().split()[3])/1024
		print str(res) + ' Mo'
	else:
		res=''
		for i in DISKS:
			res = res + str(int(os.popen("df|grep %s"%i).read().split()[3])/1024) +', '
		print res[:-2] + ' Mo'

if info == "mem_free":
	memtotal = int(os.popen("cat /proc/meminfo|grep '^MemTotal'").read().split()[1])
	memfree = int(os.popen("cat /proc/meminfo|grep '^MemFree'").read().split()[1])
	cached = int(os.popen("cat /proc/meminfo|grep '^Cached'").read().split()[1])
	buffers = int(os.popen("cat /proc/meminfo|grep '^Buffers'").read().split()[1])
	print str(memfree/1024) + "Mo"
