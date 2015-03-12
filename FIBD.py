#!/usr/bin/env python3

"""
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""

import fileinput

def fib(n, k):
	n = int(n)
	k = int(k)
	fibs = []
	for i in range(n):
		if i < 2:
			fibs.append(1)
		else:
			fibs.append(fibs[-1] + fibs[-2]*k)
	return fibs[-1]

for line in fileinput.input():
	n, k = line.split()
	print(fib(n,k))
