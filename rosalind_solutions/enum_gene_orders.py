import itertools


t = []

n = raw_input("Enter n (n < or eq 7) for the permutations:")

n = int(n)

for i in range(1,n+1):
    t.append(i)
    



k = sum(1 for x in itertools.permutations(t))

print k

for i in itertools.permutations(t):
    print ' '.join(map(str,i))
    
    