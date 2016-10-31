#euler problem 58
import math
from math import sqrt, ceil
import random
import itertools

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

p = primes_sieve(100000000)

### miller-rabin primality test
def miller_rabin(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

diag_count = 1.0
prime_count = 0.0
prime_percent = 1.0
n = 3
while prime_percent >= .1:
    diag_count +=4
    #print prime_count
    #print diag_count
    if miller_rabin(n**2 - (n - 1)) == True:
        prime_count +=1
    if miller_rabin(n**2 - 2*(n - 1)) == True:
        prime_count +=1
    if miller_rabin(n**2 - 3*(n - 1)) == True:
        prime_count +=1
    prime_percent = prime_count / diag_count
    n += 2
    
print prime_percent
print n-2

