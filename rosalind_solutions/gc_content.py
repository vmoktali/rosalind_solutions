#!/usr/bin/python

from sys import argv
from Bio import SeqIO


script, fasta_file = argv

dict = {}

for seq_record in SeqIO.parse(fasta_file, "fasta"):
    G = seq_record.seq.count("G")
    C = seq_record.seq.count("C")
    
    gc_percent = (float(G + C)/len(seq_record))*100
    
    dict[seq_record.id] = gc_percent
    
max_id = max(dict, key=dict.get)
print max_id
print dict[max_id]