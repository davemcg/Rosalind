#!/usr/bin/env python3


"""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
"""


from Bio.Seq import Seq
from Bio.Alphabet import generic_rna

import fileinput


for line in fileinput.input():
	seq = Seq(line[:-1], generic_rna)
	print(seq.translate())
