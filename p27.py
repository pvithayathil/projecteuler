#Quadtratic Primes

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

def prime(n):    
    a_list = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
    if len(a_list) == 2:
        return 1
    else:
        return 0
def cons_primes(a_list):
    count = 0
    check_number = a_list[1]
    while prime(check_number) == 1:
        count +=1
        check_number = count*count + a_list[0]*count+ a_list[1]
        if check_number < 2:
            return count
    return count

longest = [0,41,40]
for a in range(-999,999):
    for b in range(2,1000):
        ab_list = [a,b]
        temp_cons = cons_primes(ab_list)
        if temp_cons > longest[2]:
            longest = [ab_list[0],ab_list[1],temp_cons]
