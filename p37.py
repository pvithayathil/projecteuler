#p37
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

def left_to_right_prime(x, prime_list):
    x_len = len(list(str(x)))
    if(prime_list[x] == 0):
        return 0
    for i in range(1,x_len):
        if prime_list[x % (10**i)] == 0:
            return 0
    return 1
def right_to_left_prime(x, prime_list):
    x_len = len(list(str(x)))
    for i in range(0,x_len):
        #print i
        #print x / (10**i)
        #print "-----"
        if prime_list[x / (10**i)] == 0:
            return 0
    return 1

def leftright_primes(prime_list):
    p_list = []
    for i in range(10,len(prime_list)):
        if left_to_right_prime(i,prime_list) == 1 and right_to_left_prime(i,prime_list)== 1:
            p_list.append(i)
            if(len(p_list) == 11):
                return p_list
    return p_list

b = primes_sieve(10000)
a = primes_sieve(1000000)
