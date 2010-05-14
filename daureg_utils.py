#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable-msg=W0312
"""Various utility function written by myself."""
import os, tempfile
def get_result_of_cmd(cmd, max_line=10):
	"""Return the output of the commande in a string or in a file if it
	makes more than max_line (10 lines by default"""
	tmp = tempfile.NamedTemporaryFile()
	os.system(cmd+">"+tmp.name)
	nb_line = 0
	result = ""
	for line in tmp:
		nb_line += 1
		result += line
		if nb_line == max_line:
			return tmp
	return result[:-1]

