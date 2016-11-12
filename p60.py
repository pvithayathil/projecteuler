# euler project 60
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

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n%2==0 or n%3 == 0: return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0: return False
        f+= 6
    return True

p_list = prime_list(20000)
p_list = p_list[4:]

pair_list = [[3],[7],[3,7]]
temp = [[3],[7],[3,7]]
five_pair_list = []

for p in p_list:
    pair_list = temp[:]
    #print pair_list
    temp = [[p]]
    for l in pair_list:
        check = 0
        for i in l:
            a = str(i)
            b = str(p)
            if is_prime(int(a+b)) == 0 or is_prime(int(b+a)) == 0:
                check = 1
                break
                
        temp.append(l)
        if check == 0:
            t = l[:]
            t.append(p)
            if len(t) == 5:
                print t
                temp.append(t)
                five_pair_list.append(t)
            else:
                
                temp.append(t)
                
minsum = -1
for i in five_pair_list:
    if minsum == -1:
        minsum = sum(i)
    else:
        if minsum > sum(i):
            minsum = i
            
