#!/usr/bin/python

from sys import argv
from Bio import SeqIO

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr

script, fasta_file = argv

seq_list = []

for seq_record in SeqIO.parse(fasta_file, "fasta"):
    seq_list.append(seq_record.seq)
    
print long_substr(seq_list)