#p46
import math
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

def square2x(n):
    a = range(0,n+1)
    return [2*(i**2) for i in a]

def smallest_odd_not_gold(a_limit,a_prime_sieve,a_prime_list,a_square2x_list):
    ####
    for p in a_prime_list:
        for s in a_square2x_list:
            if p+s < a_limit:
                a_prime_sieve[p+s] = 1

    for i in range(2,a_limit):
        if i % 2 == 1 and a_prime_sieve[i] == 0:
            return i
    return -1

s =square2x(100)
sieve = primes_sieve(1000000)
prime = prime_list(1000000)
a = smallest_odd_not_gold(1000000,sieve,prime,s)        
