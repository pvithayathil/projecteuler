#euler47
#Euler 49
import math
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

def prime_factor(n):
    limit = int(math.sqrt(n)) + 1
    for i in range(2,limit):
        if n % i == 0:
            return [i] + prime_factor(n/i)
    return [n]

def euler47():
    i = 644
    while i < 1000000:
        if(len(list(set(prime_factor(i)))) == 4):
            if(len(list(set(prime_factor(i+1)))) == 4):
                if(len(list(set(prime_factor(i+2)))) == 4):
                    if(len(list(set(prime_factor(i+3)))) == 4):
                        return i

        i +=1
            
