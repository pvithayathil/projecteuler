#euler project 71

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)
def mult(a_list):
    t = 1
    for i in a_list:
        t = t*i
    return t

def add_list(a_list,a_element):
    for i in range(0,len(a_list)):
        if a_element < a_list[i]:
            return a_list[:i-1] + [a_element] + a_list[i-1:]
        elif a_element == a_list[i]:
            return a_list
        elif i == len(a_list) - 1:
            return a_list[:] + [a_element]

#d = 1000000
#m = mult(range(1,d+1))
#the_lcm = lcmm(*range(1,d+1))

#a = [1]
#for i in range(2,d+1):
#    for j in range(1,i):
#        a = add_list(a,j * m/i)
#num = a[a.index(m/7*3) - 1]
#
#print num / gcd(num,m)

#Project Euler Problem 71

N = 3/7.
L = 1000000
mina = N
for b in range(L, L-7, -1):
    a = N - int(b*N) * 1.0/b
    if mina > a != 0: mina, minD = a,b

print "Project Euler 71 Solution =", int(minD*N), "/", minD
        
