#!/usr/bin/python

nuc = raw_input("Enter any DNA nucleotide:")

sum_A = 0
sum_G = 0
sum_C = 0
sum_T = 0


for i in nuc:
    if "A" in i:
        sum_A = sum_A + 1
    elif "G" in i:
        sum_G = sum_G + 1
    elif "C" in i:
        sum_C = sum_C + 1
    elif "T" in i:
        sum_T = sum_T + 1
    
print sum_A, sum_C, sum_G, sum_T