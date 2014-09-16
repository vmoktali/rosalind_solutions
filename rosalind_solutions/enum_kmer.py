import itertools


t = []

s = raw_input("Enter symbols:")
n = raw_input("Enter n (n < or eq 7) for the permutations:")

n = int(n)

for i in s:
    t.append(i)

for i in itertools.product(t,repeat=n):
    print ' '.join(map(str,i))
    
    