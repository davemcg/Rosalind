#!/usr/bin/env python3

"""
Given two strings s and t of equal length, the Hamming distance 
between s and t, denoted dH(s,t), is the number of corresponding 
symbols that differ in s and t.
"""

import fileinput, itertools

def hamming(lineA, lineB):
	dist = 0
	for a,b in zip(lineA, lineB):
		if a != b:
			dist += 1
	return dist

f = fileinput.input()

for lineA, lineB in itertools.zip_longest(*[f]*2):
	print(hamming(lineA, lineB))
