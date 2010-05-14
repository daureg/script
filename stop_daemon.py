#! /usr/bin/env python
# -*- coding: utf-8 -*-
#pylint: disable-msg=W0312
""" Stop les daemons """
D = ("acpid" , "crond" , "dbus", "hal", "alsa")
for i in D:
	print ("/etc/rc.d/" + i + " stop")
