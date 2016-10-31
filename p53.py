#euler project 53

import math

limit, n, c = 1000000, 100,0

for i in range(23,n+1):
    for j in range(0,n/2 + 1):
        a = math.factorial(i)/(math.factorial(j)*math.factorial(i-j))
        if a > limit:
            c += i + 1 - 2*j

            break

print c
