#!/usr/bin/python

string1 = raw_input("Enter first string:")

string2 = raw_input("Enter second string:")

#sum = 0

print "Mismatches: %s" % [x == y for (x, y) in zip(string1, string2)].count(False)

