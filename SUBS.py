#!/usr/bin/env python3

"""
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""

import fileinput

# iterates base by base through seq1 and sees whether seq2
# matches it

def sub(seq1,seq2):
	sub_coord = []
	for i in range(0,len(seq1),1):
		if (i + len(seq2)) < len(seq1):
			if seq2 == seq1[i:(i+len(seq2))]:
				sub_coord.append(i+1) 		
		else:
			break
	return sub_coord
	

seqs = []
for line in fileinput.input():
	seqs.append(line)

seq1, seq2 = seqs[0][:-1], seqs[1][:-1]

print(*sub(seq1,seq2))
	


