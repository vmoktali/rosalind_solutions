#!/usr/bin/python

import re

string = raw_input("Enter the string to be searched:")
motif = raw_input("Enter the motif:")

#print [m.start() for m in re.finditer((?=motif), string)]

list_index = [m.start() for m in re.finditer('(?=%s)' %motif, string)]
new_list = [x+1 for x in list_index]

print '\t'.join(str(p) for p in new_list)

