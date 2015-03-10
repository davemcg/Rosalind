#!/usr/bin/env python3

"""
Given: A collection of at most 10 DNA strings of equal length 
(at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the 
collection. (If several possible consensus strings exist, 
then you may return any one of them.)
"""

import numpy as np
import fileinput
from Bio import SeqIO

fasta_file = fileinput.input()
fasta_seqs = []
for seq_record in SeqIO.parse(fasta_file,"fasta"):
	fasta_seqs.append(list(str(seq_record.seq)))

# convert to numpy array
fasta_seqs = np.asarray(fasta_seqs)

# count occurences of a,c,g,t in each column
# and add to four lists
A,C,G,T = [],[],[],[]
for column in fasta_seqs.transpose():
	A.append(sum(np.char.count(column,'A')))
	C.append(sum(np.char.count(column,'C')))
	G.append(sum(np.char.count(column,'G')))
	T.append(sum(np.char.count(column,'T')))

# create consensus sequence (most common in each column)
consensus = ''
for a,c,g,t in zip(A,C,G,T):
	if (a >= c) and (a >= g) and (a >= t):
		consensus += 'A'
	elif (c >= a) and (c >= g) and (c >= t):
		consensus += 'C'
	elif (g >= a) and (g >= c) and (g >= t):
		consensus += 'G'
	else:
		consensus += 'T'

print(consensus)
print('A:', end = ' ')
for dna in A:
	print(dna,end = ' ')
print('\n','C:', sep = '', end = ' ')
for dna in C:
	print(dna,end = ' ')
print('\n','G:', sep = '', end = ' ')
for dna in G:
	print(dna,end = ' ')
print('\n','T:', sep = '', end = ' ')
for dna in T:
	print(dna,end = ' ')



