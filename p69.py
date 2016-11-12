#euler project 69
import fractions
import math
def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount

def prime_list(n):
    a = range(0,n)                          # Initialize the primality list
    b = []
    limit = int(math.sqrt(n)) + 1
    a[0] = a[1] = 0

    for i in range(2,limit):
        if(a[i] != 0):
            m = 2
            while m*i < n:
                a[m*i] = 0
                m +=1
    for j in a:
        if j != 0:
            b.append(j)
            
    return b

primes = prime_list(1000000)
limit = 1000000
tot_fract_max = 1
for p in primes:
    tot_fract_max *= p
    if tot_fract_max > limit:
        print tot_fract_max/p
        break
    
