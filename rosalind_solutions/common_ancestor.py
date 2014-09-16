#!/usr/bin/python

from sys import argv
from Bio import SeqIO
from collections import Counter
import numpy as np
import pandas as pd

script, infile = argv

seq_list = []
seq_dict = {}
final_list = []

for seq_record in SeqIO.parse(infile, "fasta"):
    seq_list.append(list(seq_record.seq))


#print [Counter(x) for x in seq_list]
keys = ['A','C','G','T']

# make it numpy
keys = np.array(keys)
seq_list = np.array(seq_list)

# if you wanted counts for all columns (newaxis here sets-up 3D broadcasting)
counts = np.sum(keys[:,np.newaxis,np.newaxis] == seq_list, axis=1)


# view it (you could use zip without pandas, this is just for looks)


for i in counts.T:
    if i[0]>i[1] and i[0]>i[2] and i[0]>i[3]:
        final_list.append("A")
    elif i[1]>i[0] and i[1]>i[2] and i[1]>i[3]:
        final_list.append("C")
    elif i[2]>i[0] and i[2]>i[1] and i[2]>i[3]:
        final_list.append("G")
    elif i[3]>i[0] and i[3]>i[1] and i[3]>i[2]:
        final_list.append("T")

print ''.join(map(str, final_list))
print pd.DataFrame(counts, index=keys)