#p39 Integer Right Triangles

### p <= 1000
from fractions import gcd

num_sol_per = [0]*1001

### initialize
for i in range(2,1000):
    for j in range(1,i):
        if gcd(i,j) == 1:
            if (i**2 - j**2) % 2 == 1:
                abc = [2*i*j,i**2 - j**2,i**2 + j**2]
                p = sum(abc)
                n = 1
                #print "-----"
                #print [i,j]
                #print abc
                while p <= 1000:
                    num_sol_per[p] = num_sol_per[p] + 1
                    n +=1
                    abc_t = [n*i for i in abc]
                    p = sum(abc_t)


### find largest
s = 0
n = 0
for i in range(0,1001):
    if num_sol_per[i] > s:
        s = num_sol_per[i]
        n = i
print s
print n
