#!/usr/bin/env python3

"""
Read in multi-fasta files, return fasta record with highest GC content
and the GC content
"""

import fileinput
from Bio import SeqIO

fasta = fileinput.input()
fasta_dict = SeqIO.to_dict(SeqIO.parse(fasta,"fasta"))

gc_content = {}
for k,v in fasta_dict.items():
	seq = v.seq
	gc_content[k] = (seq.count('G')+seq.count('C'))/len(seq)


for k,v in ((k, gc_content[k]) for k in sorted(gc_content, key=gc_content.get, reverse=True)):
	print(k,v*100,sep="\n")	
	break
