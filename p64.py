import math


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

Limit = 10000
count = 0
for i in range(2,Limit+1):
    cf = from_root(i)
    if len(cf[1]) % 2 == 1:
        count +=1
