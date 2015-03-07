#!/usr/bin/env python3

"""
Reverse complement DNA
"""

import fileinput

def complement(line):
	output = ""
	for letter in line:
		if letter == 'A':
			output += 'T'
		elif letter == 'T':
			output += 'A'
		elif letter == 'G':
			output += 'C'
		elif letter == 'C':
			output += 'G'
	return output

for line in fileinput.input():
	reversed = line[::-1]
	print(complement(reversed))	
