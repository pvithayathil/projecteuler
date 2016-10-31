# euler problem 41
import itertools
import math
def is_pandigital(n, s=10): n=str(n); return len(n)==s and not '1234567890'[:s].strip(n)

def primes_sieve(n):
    a = [1] * n                          # Initialize the primality list
    limit = int(math.sqrt(n)) + 1
    a[0] = a[1] = 0

    for i in range(2,limit):
        if(a[i] == 1):
            m = 2
            while m*i < n:
                a[m*i] = 0
                m +=1
            
    return a

n = 7654321
p = primes_sieve(7654322)
while not(is_pandigital(n, 7) and p[n]==1):
    n -= 2

print "The largest existing n-digit pandigital prime is", n
