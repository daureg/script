#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable-msg=W0312
import os
uptime = str(os.popen('uptime').read().split()[2].strip(','))
if uptime.find(':') == -1 and int(uptime) < 5:
	print "yes"
else:
	print "no"
