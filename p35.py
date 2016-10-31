# circular primes
import math
import itertools

cprime_list = [0]*1000000

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

def list_to_number(a_list):
    l = len(a_list)-1
    n = 0
    for i in range(0,len(a_list)):
        n += (10**l)*int(a_list[i])
        l -= 1
    return n

def cir_list(n):
    c = []
    n_list = list(str(n))
    l = len(n_list)
    for i in range(0,l):
        c.append(n_list[i:]+n_list[:i])
    return c

def circular_primes(a_list):
    c_list = [0]*len(a_list)
    for i in range(2,len(a_list)):
        if(a[i] == 1 and c_list[i] == 0):
            c = cir_list(i)
            c = [list_to_number(x) for x in c]
            cprime = 1
            for j in c:
                if a[j] == 0:
                    cprime = 0
            if cprime == 1:
                for j in c:
                    c_list[j] = 1


    return c_list
