#!/usr/bin/python
import re

def replace_all(repls, str):                                     
    return re.sub('|'.join(re.escape(key) for key in repls.keys()),
                  lambda k: repls[k.group(0)], str)                                     


dna = raw_input("Enter the DNA string:")
rev_dna = replace_all({"A": "T", "T": "A", "C": "G", "G": "C"}, dna)

print "Reverse complement: %s" %rev_dna[::-1]



