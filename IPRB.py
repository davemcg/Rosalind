#!/usr/bin/env python3

"""
Given: Three positive integers k, m, and n, representing a 
population containing k+m+n organisms: k individuals are 
homozygous dominant for a factor, m are heterozygous, and 
n are homozygous recessive.

Return: The probability that two randomly selected mating 
organisms will produce an individual possessing a dominant 
allele (and thus displaying the dominant phenotype). 
Assume that any two organisms can mate.
"""

import sys
from scipy.misc import comb

# pull in k, m, n
dom, het, rec = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

# calculate total population
pop = comb(dom + het + rec, 2)

# calculate number of recessive alleles
total_rec = comb(rec, 2) + (0.5*het*rec) + (0.25*comb(het,2))
	# remember for het | rec mating half of the offspring will be rec
	# same logic (punnett squares) 1/4 of het | het mating will be rec
print(total_rec, pop, 1-total_rec/pop)
