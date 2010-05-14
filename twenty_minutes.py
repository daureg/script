#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable-msg=W0312
"""Get the lastest or a specific version of 20 minutes nantes pdf"""
import sys, os
from optparse import OptionParser
from time import gmtime, strftime

BASE_URL = "http://20minutes.s3.amazonaws.com/"
DATADIR = os.environ["HOME"] + "/data/20minutes/"

if __name__ == "__main__":
	TODAY = int(strftime("%Y%m%d", gmtime()))
	PARSER = OptionParser()
	PARSER.add_option("-d", "--date", dest="USER_DATE", default=TODAY, \
			help="date that you want (may not exist)")
	(OPTIONS, ARGS) = PARSER.parse_args()
	USER_DATE = int(OPTIONS.USER_DATE)
	if (USER_DATE > TODAY or USER_DATE < 20080101):
		USER_DATE = TODAY
	URL = BASE_URL + str(USER_DATE) + "_NAN.pdf"
	FILE = DATADIR + str(USER_DATE) + ".pdf"
	print "%s\n%s\n%s\n" %(str(USER_DATE), URL, FILE)
	os.popen("wget -O %s %s" % (FILE, URL))
	if not os.path.isfile(FILE):
		print "Le telechargement a échoué", \
				"(peut-être une mauvaise date [%s] ?)" % str(USER_DATE)
	sys.exit()
