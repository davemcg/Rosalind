#!/usr/bin/env python3

"""
Fibonacci sequence
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
			fibs.append(fibs[-1] + fibs[-2]*3)
	return fibs[-1]

for line in fileinput.input():
	n, k = line.split()
	print(fib(n,k))
