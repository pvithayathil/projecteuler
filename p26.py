def prime(n):    
    a_list = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
    if len(a_list) == 2:
        return 1
    else:
        return 0
def longest_repeat_fract(n):
    while n > 1:
        if prime(n) == 1:
            print n
            return n
        else:
            n += -1
