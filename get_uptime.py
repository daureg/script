#! /usr/bin/env python
# -*- coding: utf-8 -*-
#pylint: disable-msg=W0312
import os
print os.popen("uptime|cut -d ' ' -f5").read().strip().strip(',')
