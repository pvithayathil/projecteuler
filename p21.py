def factors(n):    
    a_list = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
    return a_list[0:1] + a_list[2:]

def amicable(n):
    return reduce(list.__add__,([i] for i in range(1,n) if sum(factors(i)) != i and sum(factors(i)) < n and i == sum(factors(sum(factors(i)))))) 
