#!/usr/bin/python


string = raw_input("Please enter a string:")
a = input("provide index for slice 1, a:")
b = input("b:")
c = input("index for slice 2, c:")
d = input("d:")



slice1 = string[a:b]
slice2 = string[c:d]

print "The two slices: %s, %s" % (slice1, slice2)
