# euler project 70
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def is_perm(a,b): return sorted(str(a))==sorted(str(b))
#set up constants
tot_ratio = 10000000.0
n = 1
upper_bound = 10000000
factor = .3
pub = int(upper_bound**.5)*(1+factor)
lub = int(upper_bound**.5)*(1-factor)
prime_list = primes(upper_bound)
bounded_prime_list = []
for p in prime_list:
    if p >= lub and p <= pub:
        bounded_prime_list.append(p)
        
for i in range(0,len(bounded_prime_list)):
    p1 = bounded_prime_list[i]
    for j in range(i+1,len(bounded_prime_list)):
        p2 = bounded_prime_list[j]
        #if (p1+p2)%9 != 1:
        tot = (p1-1)*(p2-1)
        num = p1 * p2
        if num/float(tot) < tot_ratio and num <= upper_bound:
            if is_perm(tot,num):
                tot_ratio = num/float(tot)
                n = num
                print p1,p2,n

print n, tot_ratio
