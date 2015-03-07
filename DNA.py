#!/usr/bin/env python

"""
Count A C G T
"""

import fileinput

for line in fileinput.input():
	print line.count('A'), line.count('C'), line.count('G'), line.count('T')	
