def factors_unique(n):    
    a_list = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
    a_list.sort()
    return list(set(a_list[0:len(a_list)-1]))
    



# abundant number

def is_abundant(n):
    if n <= 0:
        return 0
    elif sum(factors_unique(n)) > n:
        return n
    else:
        return 0
 

a_list = range(0,28123)
#list of abundant numbers:
a_list_abundant  = list(set(map(is_abundant,a_list)))
a_list_abundant = a_list_abundant[1:]
a_list_abundant.sort()

the_list = []

for i in range(0,len(a_list_abundant)):
    for j in range(0,len(a_list_abundant)):
        the_list.append(a_list_abundant[i]+a_list_abundant[j])
the_list = [i for i in the_list if i <=28123]

the_list = set(the_list)
a_list = set(a_list)
print sum(a_list.difference(the_list))
