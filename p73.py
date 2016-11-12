# project euler 73
from fractions import gcd

Limit = 12000
low_bound = 1/3.0
upper_bound =1/2.0
count = 0
for i in range(Limit,3,-1):
    for j in range(i/3,i):
        fract = float(j)/float(i)
        if fract > upper_bound:
            break
        elif fract > low_bound and fract < upper_bound and gcd(i,j)==1:
            count += 1

print count
            
