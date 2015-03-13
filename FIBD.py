#!/usr/bin/env python3

"""
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""

import fileinput
import numpy as np
import sys

def fibd(n, k):
	n = int(n)
	k = int(k)
	fertile = 0
#	pop = np.zeros(k, dtype = np.float64)
	pop = np.zeros(k)
	for i in range(n):
		if i <= 0:
			pop[0] = 1
		else:
			fertile = np.sum(pop[1:])
			pop = np.roll(pop,1)
			pop[0] = fertile
	return(np.sum(pop))

for line in fileinput.input():
	n, k = line.split()
	print(format(fibd(n,k), '.20f'))
