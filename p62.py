# project euler 62
from collections import defaultdict

my_dict = defaultdict(int)
#my_dict[1] += 1
my_dict = {}
#my_dict[1] = [1,1]
def LargestPerm(n):
    count_dig = [0]*10
    temp = n
    largest_n = 0
    #num_as_list = map(int,list(str(n)))
    while (temp > 0):
        count_dig[temp % 10] +=1
        temp /= 10        
    for i in range(9, -1, -1):
        while count_dig[i] != 0:
            largest_n = largest_n*10 + i
            count_dig[i] += -1
            
    return largest_n

n = 345
i = 1
while i == 1:
    p = LargestPerm(n**3)
    if p in my_dict:
         my_dict[p][0] += 1
    else:
        my_dict[p] = [1,n]
    #my_dict[p] += 1
    if my_dict[p][0] == 5:
        print my_dict[p][1]**3
        print my_dict[p][1]
        i = 0
        break
    n +=1
    
