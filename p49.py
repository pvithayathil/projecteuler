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

def euler49(p_list_four_digit,p_sieve):
    a = []
    for p in p_list_four_digit:
        p_comb = list(itertools.permutations(str(p),4))
        for i in p_comb:
            i = list(i)
            i_n = int(i[0])*1000 + int(i[1])*100+int(i[2])*10+int(i[3])
        
            s = i_n - p
            if (p_sieve[i_n] == 1 and i_n + s <= 10000 and i_n+s > p):
                if(p_sieve[i_n+s] == 1 and set(i) == set(list(str(i_n+s)))):
                    a.append( int(str(p)+str(i_n)+str(i_n+s)))
    return a
                
            
p = primes_sieve(10000)
p_list = prime_list(10000)
p_list = p_list[168:]
