#!/usr/bin/python

print("Calculate the sum of add numbers in a range A and B")
a = input("Enter A:")
b = input("B:")

sum = 0


for i in range(a,b):
    if (i % 2 != 0):
        sum = sum + i
        
print "The sum of odd integers in your range: %s" % sum