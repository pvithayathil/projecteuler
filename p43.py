#euler problem 43

import itertools

pan_list = a = list(itertools.permutations('0123456789',10))
p43_list = []

for p in pan_list:
    p = list(p)
    ### conditions
    mod = (int(p[1])*100 + int(p[2])*10 + int(p[3])) % 2
    mod += (int(p[2])*100 + int(p[3])*10 + int(p[4])) % 3
    mod += (int(p[3])*100 + int(p[4])*10 + int(p[5])) % 5
    mod += (int(p[4])*100 + int(p[5])*10 + int(p[6])) % 7
    mod += (int(p[5])*100 + int(p[6])*10 + int(p[7])) % 11
    mod += (int(p[6])*100 + int(p[7])*10 + int(p[8])) % 13
    mod += (int(p[7])*100 + int(p[8])*10 + int(p[9])) % 17

    if mod == 0:
        p43_list.append(int(p[9]) + int(p[8])*10 + int(p[7])*100 + int(p[6])*1000 + int(p[5])*10000 + int(p[4])*100000 + int(p[3])*1000000 + int(p[2])*10000000 + int(p[1])*100000000 + int(p[0])*1000000000)




    
