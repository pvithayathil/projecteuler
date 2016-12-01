import math
from fractions import gcd

def from_root(n):

    a0 = int(math.floor(math.sqrt(n)))
    r = [a0, []]
    a, b, c = 1, 2 * a0, a0 ** 2 - n
    delta = math.sqrt(4*n)

    while True:
        try:
            d = int((b + delta) / (2 * c))
        except ZeroDivisionError: # a perfect square
            return [r[0],[0,0]]
        a, b, c = c, -b + 2*c*d, a - b*d + c*d ** 2
        r[1].append(abs(d))
        if abs(a) == 1:
            break
    return r

def pell_x(i):
    cf = i[1][:(len(i[1])-1)]
    x = 0
    n = 1
    d = i[1][0]
    for c in reversed(cf):
        if x == 0:
            n = 1
            d = c
            x = 1
        else:
            t = d
            d = d*c + n
            n = t
            
    return (n + i[0]*d )/gcd(n + i[0]*d,d)

def pell2(num, i):
    i[1] = i[1] + i[1]
    n = 1
    d = i[1][0]
    if (n + i[0]*d )**2 - num*d**2 == 1:
        return (n + i[0]*d )
    
    for j in range(1,len(i[1])+1):
        
        x = 0    
        cf = i[1][:j]
        for c in reversed(cf):
            if x == 0:
                n = 1
                d = c
                x = 1
            else:
                t = d
                d = d*c + n
                n = t
        #print (n + i[0]*d )**2 - num*d**2,(n + i[0]*d ),d
        if (n + i[0]*d )**2 - num*d**2 == 1:
            return (n + i[0]*d )


    return -1

D = 1000

d,large_min_x = 0,0
for i in range(3,D+1):
    if int(D**.5) != D**.5:
        root_cf =from_root(i)
        x = pell2(i,root_cf)
        if x > large_min_x:
            d = i
            large_min_x = x
            print d
print d,large_min_x

        
