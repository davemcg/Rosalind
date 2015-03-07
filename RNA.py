#!/usr/bin/env python3


"""
DNA to RNA
"""

import fileinput

for line in fileinput.input():
	print(line.replace('T','U'))
