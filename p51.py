# euler project 51
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

a = primes_sieve(1000000)
p_list = prime_list(1000000)
p_list = p_list[9592:]

check_list = map(list,list(itertools.combinations([0,1,2,3,4],3)))
for p in p_list:
    num_as_list = map(int,list(str(p)))
    for c in check_list:
        eight_prime = 1
        if num_as_list[c[0]] == 0 or num_as_list[c[1]] == 1 or num_as_list[c[2]] == 2:
            if num_as_list[c[0]] == num_as_list[c[1]] and num_as_list[c[0]] == num_as_list[c[2]]:
                while num_as_list[c[0]] != 9:
                    num_as_list[c[0]] +=1
                    num_as_list[c[1]] +=1
                    num_as_list[c[2]] +=1
                    check_n = num_as_list[0]*100000 + num_as_list[1]*10000 + num_as_list[2]*1000 + num_as_list[3]*100 + num_as_list[4]*10 + num_as_list[5]
                    if a[check_n] == 1:
                        eight_prime +=1
                if eight_prime == 8:
                    print p
                    





        
    
