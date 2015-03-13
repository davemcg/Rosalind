#!/usr/bin/env python3

"""
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits 
that will remain after the n-th month if all 
rabbits live for m months.
"""

import fileinput

def fibd(n, m):
	pop = [1] + [0]*(m-1)
	for i in range(n-1):
		fertile = sum(pop[1:])
		pop = [fertile] + pop[:-1]
	return(sum(pop))

for line in fileinput.input():
	n, m = line.split()
	print(fibd(int(n),int(m)))
