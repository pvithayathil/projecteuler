#p50
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
### slow brute force version
def largest_consecutive_prime(prime_list,prime_limit):
    prime_sums = []
    l = 1
    lcp = 2
    for p in prime_list:
        if p == 2:
            ### iniiialize
            prime_sums.append([p])
            l = 1
            lcp = 2
        else:
            temp_prime_sums = []
            for i in prime_sums:
                temp_i = i[:]
                temp_i.append(p)
                if sum(temp_i) < prime_limit:
                    i.append(p)
                    temp_prime_sums.append(i)
                    if sum(i) in prime_list and len(i) >= l:
                        l = len(i)
                        lcp = sum(i)
            temp_prime_sums.append([p])
            prime_sums = temp_prime_sums[:]
                

    print "********"
    print l
    print lcp
    print "********"
    return lcp
#### run
#b = prime_list(1000000)
#largest_consecutive_prime(b,1000000)
    
L = 1000000
prime_sum = [0]
a = prime_list(L)
for p in prime_list(L):
	prime_sum.append(prime_sum[-1] + p)
	if prime_sum[-1] >= L: break
c = len(prime_sum)

terms = 1
for i in xrange(c):
	for j in xrange(c-1, i+terms, -1):
		n = prime_sum[j] - prime_sum[i]
		if (j-i > terms and n in a):
			terms, max_prime = j-i, n
			break

print max_prime, " with ", terms
